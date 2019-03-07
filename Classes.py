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
        self.x = x  # The x-coordinate of the piece
        self.y = y  # The y-coordinate of the piece
        self.img = pygame.image.load(Img_ID)  # The loaded image
        self.legal_moves = []  # A list that contains all the square the piece can go to

        # Initial Draw #
        window.blit(self.img, (self.x, self.y))

    def reDraw(self, window):
        window.blit(self.img, (self.x, self.y))

    def Flip_Coordinates(self):  # This method is used by black to have the board flipped
        self.x = 480 - self.x
        self.y = 540 - self.y

        return self.x, self.y

class Bishop(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

class King(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

class Knight(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

class Pawn(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self):
        self.legal_moves = []  # Clears the list
        # Top Left
        if self.x - 60 >= 0 and self.y - 60 >= 0:
            self.legal_moves.append((int(self.x - 60), int(self.y - 60)))  # Stores the row and column indexes as a tuple
        # Top Right
        if self.x + 60 <= 420 and self.y - 60 >= 0:
            self.legal_moves.append((int(self.x + 60), int(self.y - 60)))
        return self.legal_moves

class Queen(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

class Rook(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)