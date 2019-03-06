import pygame
import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.65"
        self.port = 5555
        self.addr = (self.server, self.port)

    def Make_Connection(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send_and_receive(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

class Squares:
    def __init__(self, window, x, y, color):
        self.x = x
        self.y = y
        self.color = color

        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, 60, 60))

class ChessPiece:
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        self.img = pygame.image.load(Img_ID)

        # Initial Draw #
        window.blit(self.img, (self.x, self.y))

    def reDraw(self, window):
        window.blit(self.img, (self.x, self.y))

    def Flip_Coordinates(self):  # This method is used by black to have the board flipped
        self.x = 480 - self.x
        self.y = 540 - self.y

        return self.x, self.y