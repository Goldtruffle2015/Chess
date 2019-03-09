import pygame
import socket
import pickle
import itertools

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
        self.rectangle = pygame.Rect(self.x, self.y, 60, 60)

        pygame.draw.rect(window, self.color, self.rectangle)

    def reDraw(self, window):
        pygame.draw.rect(window, self.color, self.rectangle)

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

class Bishop(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self, local, enemy):
        self.legal_moves = []

        # NorthEast
        iteration = 1
        while True:
            if self.x + 60*iteration <= 420 and self.y - 60*iteration >= 60 and not [int(self.x + 60*iteration), int(self.y - 60*iteration)] in local:
                self.legal_moves.append((int(self.x + 60*iteration), int(self.y - 60*iteration)))
                iteration += 1
            else:
                break

        # SouthEast
        iteration = 1
        while True:
            if self.x + 60*iteration <= 420 and self.y + 60*iteration <= 480 and not [int(self.x + 60*iteration), int(self.y + 60*iteration)] in local:
                self.legal_moves.append((int(self.x + 60*iteration), int(self.y + 60*iteration)))
                iteration += 1
            else:
                break

        # SouthWest
        iteration = 1
        while True:
            if self.x - 60*iteration >= 0 and self.y + 60*iteration <= 480 and not [int(self.x - 60*iteration), int(self.y + 60*iteration)] in local:
                self.legal_moves.append((int(self.x - 60*iteration), int(self.y + 60*iteration)))
                iteration += 1
            else:
                break

        # NorthWest
        iteration = 1
        while True:
            if self.x - 60*iteration >= 0 and self.y - 60*iteration >= 60 and not [int(self.x - 60*iteration), int(self.y - 60*iteration)] in local:
                self.legal_moves.append((int(self.x - 60*iteration), int(self.y - 60*iteration)))
                iteration += 1
            else:
                break

class King(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self, local, enemy):
        self.legal_moves = []
        # 1 Up
        if self.y - 60 >= 60 and not [int(self.x), int(self.y - 60)] in local:
            self.legal_moves.append((int(self.x), int(self.y - 60)))

        # 1 Right --> 1 Up
        if self.x + 60 <= 420 and self.y - 60 >= 60 and not [int(self.x + 60), int(self.y - 60)] in local:
            self.legal_moves.append((int(self.x + 60), int(self.y - 60)))

        # 1 Right
        if self.x + 60 <= 420 and not [int(self.x + 60), int(self.y)] in local:
            self.legal_moves.append((int(self.x + 60), int(self.y)))

        # 1 Right --> 1 Down
        if self.x + 60 <= 420 and self.y + 60 <= 480 and not [int(self.x + 60), int(self.y + 60)] in local:
            self.legal_moves.append((int(self.x + 60), int(self.y + 60)))

        # 1 Down
        if self.y + 60 <= 480 and not [int(self.x), int(self.y + 60)] in local:
            self.legal_moves.append((int(self.x), int(self.y + 60)))

        # 1 Left --> 1 Down
        if self.x - 60 >= 0 and self.y + 60 <= 480 and not [int(self.x - 60), int(self.y + 60)] in local:
            self.legal_moves.append((int(self.x - 60), int(self.y + 60)))

        # 1 left
        if self.x - 60 >= 0 and not [int(self.x - 60), int(self.y)] in local:
            self.legal_moves.append((int(self.x - 60), int(self.y)))

        # 1 left --> 1 UP
        if self.x - 60 >= 0 and self.y - 60 >= 60 and not [int(self.x - 60), int(self.y - 60)] in local:
            self.legal_moves.append((int(self.x - 60), int(self.y - 60)))

class Knight(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self, local, enemy):
        self.legal_moves = []
        # 1 Left --> 2 Up
        if self.x - 60 >= 0 and self.y - 120 >= 60 and not [int(self.x - 60), int(self.y - 120)] in local:
            self.legal_moves.append((int(self.x - 60), int(self.y - 120)))

        # 1 Right --> 2 Up
        if self.x + 60 <= 420 and self.y - 120 >= 60 and not [int(self.x + 60), int(self.y - 120)] in local:
            self.legal_moves.append((int(self.x + 60), int(self.y - 120)))

        # 2 Right --> 1 Up
        if self.x + 120 <= 420 and self.y - 60 >= 60 and not [int(self.x + 120), int(self.y - 60)] in local:
            self.legal_moves.append((int(self.x + 120), int(self.y - 60)))

        # 2 Right --> 1 Down
        if self.x + 120 <= 420 and self.y + 60 <= 480 and not [int(self.x + 120), int(self.y + 60)] in local:
            self.legal_moves.append((int(self.x + 120), int(self.y + 60)))

        # 1 Right --> 2 Down
        if self.x + 60 <= 420 and self.y + 120 <= 480 and not [int(self.x + 60), int(self.y + 120)] in local:
            self.legal_moves.append((int(self.x + 60), int(self.y + 120)))

        # 1 Left --> 2 Down
        if self.x - 60 >= 0 and self.y + 120 <= 480 and not [int(self.x - 60), int(self.y + 120)] in local:
            self.legal_moves.append((int(self.x - 60), int(self.y + 120)))

        # 2 Left --> 1 Down
        if self.x - 120 >= 0 and self.y + 60 <= 480 and not [int(self.x - 120), int(self.y + 60)] in local:
            self.legal_moves.append((int(self.x - 120), int(self.y + 60)))

        # 2 Left --> 1 Up
        if self.x - 120 >= 0 and self.y - 60 >= 60 and not [int(self.x - 120), int(self.y - 60)] in local:
            self.legal_moves.append((int(self.x - 120), int(self.y - 60)))

class Pawn(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self, local, enemy):
        self.legal_moves = []
        # Top Left
        if self.x - 60 >= 0 and self.y - 60 >= 60 and [int(self.x - 60), int(self.y - 60)] in enemy:  # Checks if an enemy piece is at that coordinate point
            self.legal_moves.append((int(self.x - 60), int(self.y - 60)))  # Stores the row and column indexes as a tuple
        # Top Right
        if self.x + 60 <= 420 and self.y - 60 >= 60 and [int(self.x + 60), int(self.y - 60)] in enemy:
            self.legal_moves.append((int(self.x + 60), int(self.y - 60)))
        # 1 Up
        if self.y - 60 >= 60 and not [int(self.x), int(self.y - 60)] in local:
            self.legal_moves.append((int(self.x), int(self.y - 60)))
        # 2 Up
        if self.y - 120 >= 60 and not [int(self.x), int(self.y - 120)] in local:
            self.legal_moves.append((int(self.x), int(self.y - 120)))

class Queen(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self, local, enemy):
        self.legal_moves = []

        # North
        iteration = 1  # Keeps track of the number of squares to go up by
        while True:
            if self.y - 60 * iteration >= 60 and not [int(self.x), int(self.y - 60 * iteration)] in local:
                self.legal_moves.append((int(self.x), int(self.y - 60 * iteration)))
                iteration += 1
            else:
                break

        # NorthEast
        iteration = 1
        while True:
            if self.x + 60 * iteration <= 420 and self.y - 60 * iteration >= 60 and not [int(self.x + 60 * iteration), int(self.y - 60 * iteration)] in local:
                self.legal_moves.append((int(self.x + 60 * iteration), int(self.y - 60 * iteration)))
                iteration += 1
            else:
                break

        # East
        iteration = 1
        while True:
            if self.x + 60 * iteration <= 420 and not [int(self.x + 60 * iteration), int(self.y)] in local:
                self.legal_moves.append((int(self.x + 60 * iteration), int(self.y)))
                iteration += 1
            else:
                break

        # SouthEast
        iteration = 1
        while True:
            if self.x + 60 * iteration <= 420 and self.y + 60 * iteration <= 480 and not [int(self.x + 60 * iteration), int(self.y + 60 * iteration)] in local:
                self.legal_moves.append((int(self.x + 60 * iteration), int(self.y + 60 * iteration)))
                iteration += 1
            else:
                break

        # South
        iteration = 1
        while True:
            if self.y + 60 * iteration <= 480 and not [int(self.x), int(self.y + 60 * iteration)] in local:
                self.legal_moves.append((int(self.x), int(self.y + 60 * iteration)))
                iteration += 1
            else:
                break

        # SouthWest
        iteration = 1
        while True:
            if self.x - 60 * iteration >= 0 and self.y + 60 * iteration <= 480 and not [int(self.x - 60 * iteration), int(self.y + 60 * iteration)] in local:
                self.legal_moves.append((int(self.x - 60 * iteration), int(self.y + 60 * iteration)))
                iteration += 1
            else:
                break

        # West
        iteration = 1
        while True:
            if self.x - 60 * iteration >= 0 and not [int(self.x - 60 * iteration), int(self.y)] in local:
                self.legal_moves.append((int(self.x - 60 * iteration), int(self.y)))
                iteration += 1
            else:
                break

        # NorthWest
        iteration = 1
        while True:
            if self.x - 60 * iteration >= 0 and self.y - 60 * iteration >= 60 and not [int(self.x - 60 * iteration), int(self.y - 60 * iteration)] in local:
                self.legal_moves.append((int(self.x - 60 * iteration), int(self.y - 60 * iteration)))
                iteration += 1
            else:
                break

class Rook(ChessPiece):
    def __init__(self, window, x, y, Img_ID):
        self.x = x
        self.y = y
        super().__init__(window, self.x, self.y, Img_ID)

    def getLegalMoves(self, local, enemy):
        self.legal_moves = []

        # Up
        iteration = 1  # Keeps track of the number of squares to go up by
        while True:
            if self.y - 60*iteration >= 60 and not [int(self.x), int(self.y - 60*iteration)] in local:
                self.legal_moves.append((int(self.x), int(self.y - 60*iteration)))
                iteration += 1
            else:
                break

        # Right
        iteration = 1
        while True:
            if self.x + 60*iteration <= 420 and not [int(self.x + 60*iteration), int(self.y)] in local:
                self.legal_moves.append((int(self.x + 60*iteration), int(self.y)))
                iteration += 1
            else:
                break

        # Down
        iteration = 1
        while True:
            if self.y + 60*iteration <= 480 and not [int(self.x), int(self.y + 60*iteration)] in local:
                self.legal_moves.append((int(self.x), int(self.y + 60*iteration)))
                iteration += 1
            else:
                break

        # Left
        iteration = 1
        while True:
            if self.x - 60*iteration >= 0 and not [int(self.x - 60*iteration), int(self.y)] in local:
                self.legal_moves.append((int(self.x - 60*iteration), int(self.y)))
                iteration += 1
            else:
                break