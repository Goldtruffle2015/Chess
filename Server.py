import socket
from _thread import *
import sys

server = '192.168.1.65' # Set server to local IPv4 Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(server, port)

s.listen(2) # Wait for connection from clients

def ThreatedClient(c):
    pass

while True:
    c, addr = s.accept() # Accepts connection from client