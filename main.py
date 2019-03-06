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
# Create the ChessBoard #
ChessBoard_li = []
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
Pos = n.Make_Connection()

## Make Chess Pieces
chess_pieces = [ChessPiece(window, Pos[0][0], Pos[0][1], 'RookBlack.png'), ChessPiece(window, Pos[1][0], Pos[1][1], 'KnightBlack.png'), ChessPiece(window, Pos[2][0], Pos[2][1], 'BishopBlack.png'), ChessPiece(window, Pos[3][0], Pos[3][1], 'QueenBlack.png'), ChessPiece(window, Pos[4][0], Pos[4][1], 'KingBlack.png'), ChessPiece(window, Pos[5][0], Pos[5][1], 'BishopBlack.png'), ChessPiece(window, Pos[6][0], Pos[6][1], 'KnightBlack.png'), ChessPiece(window, Pos[7][0], Pos[7][1], 'RookBlack.png'), ChessPiece(window, Pos[8][0], Pos[8][1], 'PawnBlack.png'), ChessPiece(window, Pos[9][0], Pos[9][1], 'PawnBlack.png'), ChessPiece(window, Pos[10][0], Pos[10][1], 'PawnBlack.png'), ChessPiece(window, Pos[11][0], Pos[11][1], 'PawnBlack.png'), ChessPiece(window, Pos[12][0], Pos[12][1], 'PawnBlack.png'), ChessPiece(window, Pos[13][0], Pos[13][1], 'PawnBlack.png'), ChessPiece(window, Pos[14][0], Pos[14][1], 'PawnBlack.png'), ChessPiece(window, Pos[15][0], Pos[15][1], 'PawnBlack.png'), ChessPiece(window, Pos[16][0], Pos[16][1], 'PawnWhite.png'), ChessPiece(window, Pos[17][0], Pos[17][1], 'PawnWhite.png'), ChessPiece(window, Pos[18][0], Pos[18][1], 'PawnWhite.png'), ChessPiece(window, Pos[19][0], Pos[19][1], 'PawnWhite.png'), ChessPiece(window, Pos[20][0], Pos[20][1], 'PawnWhite.png'), ChessPiece(window, Pos[21][0], Pos[21][1], 'PawnWhite.png'), ChessPiece(window, Pos[22][0], Pos[22][1], 'PawnWhite.png'), ChessPiece(window, Pos[23][0], Pos[23][1], 'PawnWhite.png'), ChessPiece(window, Pos[24][0], Pos[24][1], 'RookWhite.png'), ChessPiece(window, Pos[25][0], Pos[25][1], 'KnightWhite.png'), ChessPiece(window, Pos[26][0], Pos[26][1], 'BishopWhite.png'), ChessPiece(window, Pos[27][0], Pos[27][1], 'QueenWhite.png'), ChessPiece(window, Pos[28][0], Pos[28][1], 'KingWhite.png'), ChessPiece(window, Pos[29][0], Pos[29][1], 'BishopWhite.png'), ChessPiece(window, Pos[30][0], Pos[30][1], 'KnightWhite.png'), ChessPiece(window, Pos[31][0], Pos[31][1], 'RookWhite.png')]

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    pygame.display.update()

pygame.quit()