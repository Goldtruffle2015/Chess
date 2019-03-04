import socket

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Sets the client
        self.server = '192.168.1.65' # Set server to local device
        self.port = 5555
        self.address = (self.server, self.port) # Binds the server and port

    def Connect(self):
        try:
            self.client.connect(self.address) # Client will attempt to connect to server
            return self.client.recv(2048).decode() # Return data sent from the server
        except:
            pass

    def Send(self, data):
        try:
            pass
        except socket.error as e:
            print(e)