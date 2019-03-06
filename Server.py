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

Positions = [(0, 60), (60, 60), (120, 60), (180, 60), (240, 60), (300, 60), (360, 60), (420, 60), (0, 120), (60, 120), (120, 120), (180, 120), (240, 120), (300, 120), (360, 120), (420, 120), (0, 420), (60, 420), (120, 420), (180, 420), (240, 420), (300, 420), (360, 420), (420, 420), (0, 480), (60, 480), (120, 480), (180, 480), (240, 480), (300, 480), (360, 480), (420, 480)]

def ThreatedClient(conn, ):
    conn.send(pickle.dumps(Positions))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))  # Get changes made by the client
            if not data:  # When no changes are received
                print('Disconnected...')
                break
            else:
                reply = pickle.dumps(data)
        except:
            break

    print('Connection Lost ... ')
    conn.close()

while True:
    c, address = s.accept()  # Accepts connection from client
    print('Connected to:', address)

    start_new_thread(ThreatedClient, (c, ))