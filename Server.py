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

# Index 0: All piece positions
    # Index 0: x-coordinate
    # Index 1: y-coordinate
    # Index 2: Piece ID
    # Piece ID's:
'''
A8 Black Rook: 0
B8 Black Knight: 1
C8 Black Bishop: 2
Black Queen: 3
Black King: 4
F8 Black Bishop: 5
G8 Black Knight: 6
H8 Black Rook: 7
A7 Black Pawn: 8
B7 Black Pawn: 9
C7 Black Pawn: 10
D7 Black Pawn: 11
E7 Black Pawn: 12
F7 Black Pawn: 13
G7 Black Pawn: 14
H7 Black Pawn: 15

A2 White Pawn: 16
B2 White Pawn: 17
C2 White Pawn: 18
D2 White Pawn: 19
E2 White Pawn: 20
F2 White Pawn: 21
G2 White Pawn: 22
H2 White Pawn: 23
A1 White Rook: 24
B1 White Knight: 25
C1 White Bishop: 26
White Queen: 27
White King: 28
F1 White Bishop: 29
G1 White Knight: 30
H1 White Rook: 31
'''
# Index 1: # Previous Piece Position
# Index 2: New piece position
Data = [[[0, 60, 0], [60, 60, 1], [120, 60, 2], [180, 60, 3], [240, 60, 4], [300, 60, 5], [360, 60, 6], [420, 60, 7], [0, 120, 8], [60, 120, 9], [120, 120, 10], [180, 120, 11], [240, 120, 12], [300, 120, 13], [360, 120, 14], [420, 120, 15], [0, 420, 16], [60, 420, 17], [120, 420, 18], [180, 420, 19], [240, 420, 20], [300, 420, 21], [360, 420, 22], [420, 420, 23], [0, 480, 24], [60, 480, 25], [120, 480, 26], [180, 480, 27], [240, 480, 28], [300, 480, 29], [360, 480, 30], [420, 480, 31]], '']  # Starting positions of the pieces

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
            if player == 1:  # Black
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