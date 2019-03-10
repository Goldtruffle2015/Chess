'''
Title: Chess
Author: John Yu
Date: 2019-03-03
'''

import math
from Classes import *
import pygame

def resetBoard(squares, pieces):  # Used to draw over the stars from the board
    # Redraw the squares #
    for s in squares:
        s.reDraw(window)

    # Redraw the local pieces #
    for l in pieces[0]:
        l.reDraw(window)

    # Redraw the enemy pieces #
    for e in pieces[1]:
        e.reDraw(window)

def get_board_state(local, enemy):
    local_pieces = []  # Keeps track of the position of the player's pieces
    enemy_pieces = []  # Keeps track of the position of the enemy's pieces

    for i in range(16):  # Local pieces
        local_pieces.append(local[i][:2])
    for i in range(16):  # Enemy pieces
        enemy_pieces.append(enemy[i][:2])

    return local_pieces, enemy_pieces

dictionary_of_image_IDs = {
    1: 'RookBlack.png',
    2: 'KnightBlack.png',
    3: 'BishopBlack.png',
    4: 'QueenBlack.png',
    5: 'KingBlack.png',
    6: 'PawnBlack.png',
    7: 'PawnWhite.png',
    8: 'RookWhite.png',
    9: 'KnightWhite.png',
    10: 'BishopWhite.png',
    11: 'QueenWhite.png',
    12: 'KingWhite.png'
}

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
local_piece_info = n.Make_Connection()

## Make Chess Pieces
local = [Pawn(window, local_piece_info[0][0], local_piece_info[0][1], local_piece_info[0][2], dictionary_of_image_IDs[local_piece_info[0][3]]), Pawn(window, local_piece_info[1][0], local_piece_info[1][1], local_piece_info[1][2], dictionary_of_image_IDs[local_piece_info[1][3]]), Pawn(window, local_piece_info[2][0], local_piece_info[2][1], local_piece_info[2][2], dictionary_of_image_IDs[local_piece_info[2][3]]), Pawn(window, local_piece_info[3][0], local_piece_info[3][1], local_piece_info[3][2], dictionary_of_image_IDs[local_piece_info[3][3]]), Pawn(window, local_piece_info[4][0], local_piece_info[4][1], local_piece_info[4][2], dictionary_of_image_IDs[local_piece_info[4][3]]), Pawn(window, local_piece_info[5][0], local_piece_info[5][1], local_piece_info[5][2], dictionary_of_image_IDs[local_piece_info[5][3]]), Pawn(window, local_piece_info[6][0], local_piece_info[6][1], local_piece_info[6][2], dictionary_of_image_IDs[local_piece_info[6][3]]), Pawn(window, local_piece_info[7][0], local_piece_info[7][1], local_piece_info[7][2], dictionary_of_image_IDs[local_piece_info[7][3]]), Rook(window, local_piece_info[8][0], local_piece_info[8][1], local_piece_info[8][2], dictionary_of_image_IDs[local_piece_info[8][3]]), Knight(window, local_piece_info[9][0], local_piece_info[9][1], local_piece_info[9][2], dictionary_of_image_IDs[local_piece_info[9][3]]), Bishop(window, local_piece_info[10][0], local_piece_info[10][1], local_piece_info[10][2], dictionary_of_image_IDs[local_piece_info[10][3]]), Queen(window, local_piece_info[11][0], local_piece_info[11][1], local_piece_info[11][2], dictionary_of_image_IDs[local_piece_info[11][3]]), King(window, local_piece_info[12][0], local_piece_info[12][1], local_piece_info[12][2], dictionary_of_image_IDs[local_piece_info[12][3]]), Bishop(window, local_piece_info[13][0], local_piece_info[13][1], local_piece_info[13][2], dictionary_of_image_IDs[local_piece_info[13][3]]), Knight(window, local_piece_info[14][0], local_piece_info[14][1], local_piece_info[14][2], dictionary_of_image_IDs[local_piece_info[14][3]]), Rook(window, local_piece_info[15][0], local_piece_info[15][1], local_piece_info[15][2], dictionary_of_image_IDs[local_piece_info[15][3]])]

enemy_piece_info = n.send_and_receive(local_piece_info)

enemy = [Rook(window, enemy_piece_info[0][0], enemy_piece_info[0][1], enemy_piece_info[0][2], dictionary_of_image_IDs[enemy_piece_info[0][3]]), Knight(window, enemy_piece_info[1][0], enemy_piece_info[1][1], enemy_piece_info[1][2], dictionary_of_image_IDs[enemy_piece_info[1][3]]), Bishop(window, enemy_piece_info[2][0], enemy_piece_info[2][1], enemy_piece_info[2][2], dictionary_of_image_IDs[enemy_piece_info[2][3]]), Queen(window, enemy_piece_info[3][0], enemy_piece_info[3][1], enemy_piece_info[3][2], dictionary_of_image_IDs[enemy_piece_info[3][3]]), King(window, enemy_piece_info[4][0], enemy_piece_info[4][1], enemy_piece_info[4][2], dictionary_of_image_IDs[enemy_piece_info[4][3]]), Bishop(window, enemy_piece_info[5][0], enemy_piece_info[5][1], enemy_piece_info[5][2], dictionary_of_image_IDs[enemy_piece_info[5][3]]), Knight(window, enemy_piece_info[6][0], enemy_piece_info[6][1], enemy_piece_info[6][2], dictionary_of_image_IDs[enemy_piece_info[6][3]]), Rook(window, enemy_piece_info[7][0], enemy_piece_info[7][1], enemy_piece_info[7][2], dictionary_of_image_IDs[enemy_piece_info[7][3]]), Pawn(window, enemy_piece_info[8][0], enemy_piece_info[8][1], enemy_piece_info[8][2], dictionary_of_image_IDs[enemy_piece_info[8][3]]), Pawn(window, enemy_piece_info[9][0], enemy_piece_info[9][1], enemy_piece_info[9][2], dictionary_of_image_IDs[enemy_piece_info[9][3]]), Pawn(window, enemy_piece_info[10][0], enemy_piece_info[10][1], enemy_piece_info[10][2], dictionary_of_image_IDs[enemy_piece_info[10][3]]), Pawn(window, enemy_piece_info[11][0], enemy_piece_info[11][1], enemy_piece_info[11][2], dictionary_of_image_IDs[enemy_piece_info[11][3]]), Pawn(window, enemy_piece_info[12][0], enemy_piece_info[12][1], enemy_piece_info[12][2], dictionary_of_image_IDs[enemy_piece_info[12][3]]), Pawn(window, enemy_piece_info[13][0], enemy_piece_info[13][1], enemy_piece_info[13][2], dictionary_of_image_IDs[enemy_piece_info[13][3]]), Pawn(window, enemy_piece_info[14][0], enemy_piece_info[14][1], enemy_piece_info[14][2], dictionary_of_image_IDs[enemy_piece_info[14][3]]), Pawn(window, enemy_piece_info[15][0], enemy_piece_info[15][1], enemy_piece_info[15][2], dictionary_of_image_IDs[enemy_piece_info[15][3]])]

chess_pieces = [local, enemy]

clock = pygame.time.Clock()

run = True
# Game Starts Here #
while run:
    clock.tick(60)
    
    enemy_piece_info = n.send_and_receive(local_piece_info)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    m1, m2, m3 = pygame.mouse.get_pressed()
    if m1:  # When the left mouse button is pressed
        m_pos = pygame.mouse.get_pos()  # Returns a tuple with x and y coordinates of mouse

        local_pos, enemy_pos = get_board_state(local_piece_info, enemy_piece_info)
        for piece in chess_pieces[0]:  # Finds the piece that the player clicked on
            if piece.x <= m_pos[0] < piece.x + 60 and piece.y <= m_pos[1] < piece.y + 60:
                resetBoard(ChessBoard_li, chess_pieces)  # Blit the current board layout
                piece.legal_moves = []  # Clears the list
                piece.getLegalMoves(local_pos, enemy_pos)  # Returns a list of coordinates to display
                for coordinates in piece.legal_moves:
                    window.blit(star, (coordinates[0], coordinates[1]))
                break

    pygame.display.update()

pygame.quit()