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

    # Redraw the white pieces #
    for w in pieces[0]:
        w.reDraw(window)

    # Redraw the black pieces #
    for b in pieces[1]:
        b.reDraw(window)

def get_board_state(data_list):
    local_pieces = []  # Keeps track of the position of the player's pieces
    enemy_pieces = []  # Keeps track of the position of the enemy's pieces
    if data_list[1] == 0:  # If player is white
        for i in range(16, 31):  # White pieces
            local_pieces.append(data_list[0][i][:2])
        for i in range(16):  # Black pieces
            enemy_pieces.append(data_list[0][i][:2])
    elif data_list[1] == 1:  # If player is black
        for i in range(16):  # Black pieces
            local_pieces.append(data_list[0][i][:2])
        for i in range(16, 31):  # White pieces
            enemy_pieces.append(data_list[0][i][:2])
    return local_pieces, enemy_pieces

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
local_player = player()
local_player.data = n.Make_Connection()

## Make Chess Pieces
white = [Pawn(window, local_player.data[0][16][0], local_player.data[0][16][1], local_player.data[0][16][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][17][0], local_player.data[0][17][1], local_player.data[0][17][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][18][0], local_player.data[0][18][1], local_player.data[0][18][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][19][0], local_player.data[0][19][1], local_player.data[0][19][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][20][0], local_player.data[0][20][1], local_player.data[0][20][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][21][0], local_player.data[0][21][1], local_player.data[0][21][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][22][0], local_player.data[0][22][1], local_player.data[0][22][2], 'PawnWhite.png'), Pawn(window, local_player.data[0][23][0], local_player.data[0][23][1], local_player.data[0][23][2], 'PawnWhite.png'), Rook(window, local_player.data[0][24][0], local_player.data[0][24][1], local_player.data[0][24][2], 'RookWhite.png'), Knight(window, local_player.data[0][25][0], local_player.data[0][25][1], local_player.data[0][25][2], 'KnightWhite.png'), Bishop(window, local_player.data[0][26][0], local_player.data[0][26][1], local_player.data[0][26][2], 'BishopWhite.png'), Queen(window, local_player.data[0][27][0], local_player.data[0][27][1], local_player.data[0][27][2], 'QueenWhite.png'), King(window, local_player.data[0][28][0], local_player.data[0][28][1], local_player.data[0][28][2], 'KingWhite.png'), Bishop(window, local_player.data[0][29][0], local_player.data[0][29][1], local_player.data[0][29][2], 'BishopWhite.png'), Knight(window, local_player.data[0][30][0], local_player.data[0][30][1], local_player.data[0][30][2], 'KnightWhite.png'), Rook(window, local_player.data[0][31][0], local_player.data[0][31][1], local_player.data[0][31][2], 'RookWhite.png')]

black = [Rook(window, local_player.data[0][0][0], local_player.data[0][0][1], local_player.data[0][0][2], 'RookBlack.png'), Knight(window, local_player.data[0][1][0], local_player.data[0][1][1], local_player.data[0][1][2], 'KnightBlack.png'), Bishop(window, local_player.data[0][2][0], local_player.data[0][2][1], local_player.data[0][2][2], 'BishopBlack.png'), Queen(window, local_player.data[0][3][0], local_player.data[0][3][1], local_player.data[0][3][2], 'QueenBlack.png'), King(window, local_player.data[0][4][0], local_player.data[0][4][1], local_player.data[0][4][2], 'KingBlack.png'), Bishop(window, local_player.data[0][5][0], local_player.data[0][5][1], local_player.data[0][5][2], 'BishopBlack.png'), Knight(window, local_player.data[0][6][0], local_player.data[0][6][1], local_player.data[0][6][2], 'KnightBlack.png'), Rook(window, local_player.data[0][7][0], local_player.data[0][7][1], local_player.data[0][7][2], 'RookBlack.png'), Pawn(window, local_player.data[0][8][0], local_player.data[0][8][1], local_player.data[0][8][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][9][0], local_player.data[0][9][1], local_player.data[0][9][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][10][0], local_player.data[0][10][1], local_player.data[0][10][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][11][0], local_player.data[0][11][1], local_player.data[0][11][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][12][0], local_player.data[0][12][1], local_player.data[0][12][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][13][0], local_player.data[0][13][1], local_player.data[0][13][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][14][0], local_player.data[0][14][1], local_player.data[0][14][2], 'PawnBlack.png'), Pawn(window, local_player.data[0][15][0], local_player.data[0][15][1], local_player.data[0][15][2], 'PawnBlack.png')]

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

        local_player.local_pos, local_player.enemy_pos = get_board_state(local_player.data)  # Get the state of the board
        for piece in chess_pieces[local_player.data[1]]:  # Finds the piece that the player clicked on
            if piece.x <= m_pos[0] < piece.x + 60 and piece.y <= m_pos[1] < piece.y + 60:
                local_player.selected_piece = piece
                resetBoard(ChessBoard_li, chess_pieces)  # Blit the current board layout
                piece.legal_moves = []  # Clears the list
                piece.getLegalMoves(local_player.local_pos, local_player.enemy_pos)  # Returns a list of coordinates to display
                local_player.legal_move = piece.legal_moves
                for coordinates in piece.legal_moves:
                    window.blit(star, (coordinates[0], coordinates[1]))
                break

        for move in local_player.legal_move:
            if move[0] <= m_pos[0] < move[0] + 60 and move[1] <= m_pos[1] < move[1] + 60:
                ### --- Move the piece to selected square --- ###
                local_player.selected_piece.x = move[0]
                local_player.selected_piece.y = move[1]
                local_player.selected_piece.reDraw(window)

                ### --- Update the Data List --- ###
                for piece_info in local_player.data[0]:
                    if local_player.selected_piece.id == piece_info[2]:
                        piece_info[0] = local_player.selected_piece.x
                        piece_info[1] = local_player.selected_piece.y

    local_player.data = n.send_and_receive(local_player.data)

    pygame.display.update()

pygame.quit()