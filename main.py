'''
Title: Chess
Author: John Yu
Date: 2019-03-03
'''

import math
from Classes import *
import pygame

pygame.init()  # Initialize pygame

windowx = 720
windowy = 600
window = pygame.display.set_mode((windowx, windowy)) # Creates the window
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

window.fill((200, 200, 200)) # Create Background

# Create star
star = pygame.image.load('Star.png')
# Create the chessboard #
ChessBoard_li = []  # Keeps track of all the square on the chess
ChessBoardColors = [(255, 222, 173), (139, 69, 19)] # Colors: Navajowhite, Saddlebrown
for i in range(64):
    x = (i % 8) * 60
    column = (i % 8)
    y = (math.floor(i / 8) * 60) + 60
    row = math.floor(i / 8)
    ChessBoard_li.append(Squares(window, x, y, ChessBoardColors[(column + row) % 2]))

# Create Control Panel #
    # Background #
pygame.draw.rect(window, (255, 255, 255), pygame.Rect(485, 0, 235, 600))

# Code Starts Here #
n = Network()
Data = n.Make_Connection()

## Make Chess Pieces
white = [Pawn(window, Data[0][16][0], Data[0][16][1], 'PawnWhite.png'), Pawn(window, Data[0][17][0], Data[0][17][1], 'PawnWhite.png'), Pawn(window, Data[0][18][0], Data[0][18][1], 'PawnWhite.png'), Pawn(window, Data[0][19][0], Data[0][19][1], 'PawnWhite.png'), Pawn(window, Data[0][20][0], Data[0][20][1], 'PawnWhite.png'), Pawn(window, Data[0][21][0], Data[0][21][1], 'PawnWhite.png'), Pawn(window, Data[0][22][0], Data[0][22][1], 'PawnWhite.png'), Pawn(window, Data[0][23][0], Data[0][23][1], 'PawnWhite.png'), Rook(window, Data[0][24][0], Data[0][24][1], 'RookWhite.png'), Knight(window, Data[0][25][0], Data[0][25][1], 'KnightWhite.png'), Bishop(window, Data[0][26][0], Data[0][26][1], 'BishopWhite.png'), Queen(window, Data[0][27][0], Data[0][27][1], 'QueenWhite.png'), King(window, Data[0][28][0], Data[0][28][1], 'KingWhite.png'), Bishop(window, Data[0][29][0], Data[0][29][1], 'BishopWhite.png'), Knight(window, Data[0][30][0], Data[0][30][1], 'KnightWhite.png'), Rook(window, Data[0][31][0], Data[0][31][1], 'RookWhite.png')]

black = [Rook(window, Data[0][0][0], Data[0][0][1], 'RookBlack.png'), Knight(window, Data[0][1][0], Data[0][1][1], 'KnightBlack.png'), Bishop(window, Data[0][2][0], Data[0][2][1], 'BishopBlack.png'), Queen(window, Data[0][3][0], Data[0][3][1], 'QueenBlack.png'), King(window, Data[0][4][0], Data[0][4][1], 'KingBlack.png'), Bishop(window, Data[0][5][0], Data[0][5][1], 'BishopBlack.png'), Knight(window, Data[0][6][0], Data[0][6][1], 'KnightBlack.png'), Rook(window, Data[0][7][0], Data[0][7][1], 'RookBlack.png'), Pawn(window, Data[0][8][0], Data[0][8][1], 'PawnBlack.png'), Pawn(window, Data[0][9][0], Data[0][9][1], 'PawnBlack.png'), Pawn(window, Data[0][10][0], Data[0][10][1], 'PawnBlack.png'), Pawn(window, Data[0][11][0], Data[0][11][1], 'PawnBlack.png'), Pawn(window, Data[0][12][0], Data[0][12][1], 'PawnBlack.png'), Pawn(window, Data[0][13][0], Data[0][13][1], 'PawnBlack.png'), Pawn(window, Data[0][14][0], Data[0][14][1], 'PawnBlack.png'), Pawn(window, Data[0][15][0], Data[0][15][1], 'PawnBlack.png')]

chess_pieces = [white, black]

clock = pygame.time.Clock()

run = True
# Game Starts Here #
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    m1, m2, m3 = pygame.mouse.get_pressed()
    if m1:  # When the left mouse button is pressed
        m_pos = pygame.mouse.get_pos()  # Returns a tuple with x and y coordinates of mouse

        for piece in chess_pieces[Data[1]]:
            if m_pos[0] >= piece.x and m_pos[0] < piece.x + 60 and m_pos[1] >= piece.y and m_pos[1] < piece.y + 60:
                legal_moves = piece.getLegalMoves()  # Returns a list of coordinates to display
                for coordinates in legal_moves:
                    window.blit(star, (coordinates[0], coordinates[1]))

    pygame.display.update()

pygame.quit()