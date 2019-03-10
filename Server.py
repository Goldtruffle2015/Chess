import socket
from _thread import *
import pickle
from Classes import *

server = '192.168.1.65'  # Set server to local IPv4 Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)  # Wait for connection from clients
print('Waiting for a connection, Server Started ...')

# Index 1 is x-coordinate
# Index 2 is y-coordinate
# Index 3 is piece id
# Index 4 is image id
white = [[0, 420, 16, 7], [60, 420, 17, 7], [120, 420, 18, 7], [180, 420, 19, 7], [240, 420, 20, 7], [300, 420, 21, 7], [360, 420, 22, 7], [420, 420, 23, 7], [0, 480, 24, 8], [60, 480, 25, 9], [120, 480, 26, 10], [180, 480, 27, 11], [240, 480, 28, 12], [300, 480, 29, 10], [360, 480, 30, 9], [420, 480, 31, 8]]
black = [[0, 120, 8, 6], [60, 120, 9, 6], [120, 120, 10, 6], [180, 120, 11, 6], [240, 120, 12, 6], [300, 120, 13, 6], [360, 120, 14, 6], [420, 120, 15, 6], [0, 60, 0, 1], [60, 60, 1, 2], [120, 60, 2, 3], [180, 60, 3, 4], [240, 60, 4, 5], [300, 60, 5, 3], [360, 60, 6, 2], [420, 60, 7, 1]]

pieces = [white, black]

def ThreatedClient(conn, player):
    if player == 1: # Black
        # Flip the coordinates
        for coordinates in pieces[1]:
            coordinates[0] = 420 - coordinates[0]
            coordinates[1] = 540 - coordinates[1]
    conn.send(pickle.dumps(pieces[player]))  # Send the starting positions of pieces to client
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            if player == 1:  # Black
                # Flip the coordinates
                for coordinates in new_data:
                    coordinates[0] = 420 - coordinates[0]
                    coordinates[1] = 540 - coordinates[1]
            pieces[player] = new_data
            if not new_data:
                print('Disconnected...')
                break
            else:
                if player == 0:
                    reply = pickle.dumps(pieces[1])
                if player == 1:
                    for coordinates in pieces[0]:
                        coordinates[0] = 420 - coordinates[0]
                        coordinates[1] = 540 - coordinates[1]
                    reply = pickle.dumps(pieces[0])

            conn.sendall(reply)  # Send reply to clients
        except:
            break

    print('Connection Lost ... ')
    conn.close()

current_player = 0
while True:
    c, address = s.accept()  # Accepts connection from client
    print('Connected to:', address)

    start_new_thread(ThreatedClient, (c, current_player))
    current_player += 1