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

Data = [[[0, 60], [60, 60], [120, 60], [180, 60], [240, 60], [300, 60], [360, 60], [420, 60], [0, 120], [60, 120], [120, 120], [180, 120], [240, 120], [300, 120], [360, 120], [420, 120], [0, 420], [60, 420], [120, 420], [180, 420], [240, 420], [300, 420], [360, 420], [420, 420], [0, 480], [60, 480], [120, 480], [180, 480], [240, 480], [300, 480], [360, 480], [420, 480]], '']

def ThreatedClient(conn, player):
    if player == 0: # White
        Data[1] = 0  # 0 denotes white
    elif player == 1: # Black
        Data[1] = 1  # 1 denotes black

    if player == 1: # Black
        # Flip the coordinates
        for coordinates in Data[0]:
            coordinates[0] = 420 - coordinates[0]
            coordinates[1] = 540 - coordinates[1]
    conn.send(pickle.dumps(Data))  # Send the starting positions of pieces to client
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            if player == 1:
                # Flip the coordinates
                for coordinates in new_data[0]:
                    coordinates[0] = 420 - coordinates[0]
                    coordinates[1] = 540 - coordinates[1]
            if not new_data:
                print('Disconnected...')
                break
            else:
                if player == 1:
                    for coordinates in new_data[0]:
                        coordinates[0] = 420 - coordinates[0]
                        coordinates[1] = 540 - coordinates[1]
                reply = pickle.dumps(new_data)  # Send the data to white

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