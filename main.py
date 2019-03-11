'''
Title: Chess
Author: John Yu
Date: 2019-03-03
'''

import math
from Classes import *
import pygame
from pygame.locals import *

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

def flip_coordinates(list):
    for coordinates in list:
        coordinates[0] = 420 - coordinates[0]
        coordinates[1] = 540 - coordinates[1]
    return list

def reDraw_window(squares_list, local_piece_list, enemy_piece_list):
    # Redraw all the chess squares #
    for squares in squares_list:
        squares.reDraw(window)

    # Redraw local pieces #
    for piece in local_piece_list:
        piece.reDraw(window)

    # Redraw enemy pieces #
    for piece in enemy_piece_list:
        piece.reDraw(window)

def draw_stars(legal_moves):
    for coordinates in legal_moves:
        window.blit(star, (coordinates[0], coordinates[1]))

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
pygame.font.init()

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
pygame.draw.rect(window, (240, 240, 240), pygame.Rect(485, 0, 235, 600))

# Create display that shows who moves #
pygame.draw.rect(window, (255, 255, 255), pygame.Rect(490, 5, 225, 70))

# Create Font Objects#
player_move_WHITE = pygame.font.SysFont('Bookman Old Style', 60)
player_move_BLACK = pygame.font.SysFont('Bookman Old Style', 60)
player_move_TEXT = [player_move_WHITE, player_move_BLACK]

# Code Starts Here #
n = Network()
local_player = player()
local_piece_info = n.Make_Connection()

# Flip coordinates if player is black
if local_piece_info[0] == 1:  # If player is black
    flip_coordinates(local_piece_info[1])

## Make Chess Pieces
local = [Pawn(window, local_piece_info[1][0][0], local_piece_info[1][0][1], local_piece_info[1][0][2], dictionary_of_image_IDs[local_piece_info[1][0][3]]), Pawn(window, local_piece_info[1][1][0], local_piece_info[1][1][1], local_piece_info[1][1][2], dictionary_of_image_IDs[local_piece_info[1][1][3]]), Pawn(window, local_piece_info[1][2][0], local_piece_info[1][2][1], local_piece_info[1][2][2], dictionary_of_image_IDs[local_piece_info[1][2][3]]), Pawn(window, local_piece_info[1][3][0], local_piece_info[1][3][1], local_piece_info[1][3][2], dictionary_of_image_IDs[local_piece_info[1][3][3]]), Pawn(window, local_piece_info[1][4][0], local_piece_info[1][4][1], local_piece_info[1][4][2], dictionary_of_image_IDs[local_piece_info[1][4][3]]), Pawn(window, local_piece_info[1][5][0], local_piece_info[1][5][1], local_piece_info[1][5][2], dictionary_of_image_IDs[local_piece_info[1][5][3]]), Pawn(window, local_piece_info[1][6][0], local_piece_info[1][6][1], local_piece_info[1][6][2], dictionary_of_image_IDs[local_piece_info[1][6][3]]), Pawn(window, local_piece_info[1][7][0], local_piece_info[1][7][1], local_piece_info[1][7][2], dictionary_of_image_IDs[local_piece_info[1][7][3]]), Rook(window, local_piece_info[1][8][0], local_piece_info[1][8][1], local_piece_info[1][8][2], dictionary_of_image_IDs[local_piece_info[1][8][3]]), Knight(window, local_piece_info[1][9][0], local_piece_info[1][9][1], local_piece_info[1][9][2], dictionary_of_image_IDs[local_piece_info[1][9][3]]), Bishop(window, local_piece_info[1][10][0], local_piece_info[1][10][1], local_piece_info[1][10][2], dictionary_of_image_IDs[local_piece_info[1][10][3]]), Queen(window, local_piece_info[1][11][0], local_piece_info[1][11][1], local_piece_info[1][11][2], dictionary_of_image_IDs[local_piece_info[1][11][3]]), King(window, local_piece_info[1][12][0], local_piece_info[1][12][1], local_piece_info[1][12][2], dictionary_of_image_IDs[local_piece_info[1][12][3]]), Bishop(window, local_piece_info[1][13][0], local_piece_info[1][13][1], local_piece_info[1][13][2], dictionary_of_image_IDs[local_piece_info[1][13][3]]), Knight(window, local_piece_info[1][14][0], local_piece_info[1][14][1], local_piece_info[1][14][2], dictionary_of_image_IDs[local_piece_info[1][14][3]]), Rook(window, local_piece_info[1][15][0], local_piece_info[1][15][1], local_piece_info[1][15][2], dictionary_of_image_IDs[local_piece_info[1][15][3]])]

if local_piece_info[0] == 1:
    flip_coordinates(local_piece_info[1])
enemy_piece_info = n.send_and_receive(local_piece_info)
if local_piece_info[0] == 1:
    flip_coordinates(local_piece_info[1])

# Flip coordinates if player is black
if enemy_piece_info[0] == 0:  # If enemy is white
    flip_coordinates(enemy_piece_info[1])

enemy = [Rook(window, enemy_piece_info[1][0][0], enemy_piece_info[1][0][1], enemy_piece_info[1][0][2], dictionary_of_image_IDs[enemy_piece_info[1][0][3]]), Knight(window, enemy_piece_info[1][1][0], enemy_piece_info[1][1][1], enemy_piece_info[1][1][2], dictionary_of_image_IDs[enemy_piece_info[1][1][3]]), Bishop(window, enemy_piece_info[1][2][0], enemy_piece_info[1][2][1], enemy_piece_info[1][2][2], dictionary_of_image_IDs[enemy_piece_info[1][2][3]]), Queen(window, enemy_piece_info[1][3][0], enemy_piece_info[1][3][1], enemy_piece_info[1][3][2], dictionary_of_image_IDs[enemy_piece_info[1][3][3]]), King(window, enemy_piece_info[1][4][0], enemy_piece_info[1][4][1], enemy_piece_info[1][4][2], dictionary_of_image_IDs[enemy_piece_info[1][4][3]]), Bishop(window, enemy_piece_info[1][5][0], enemy_piece_info[1][5][1], enemy_piece_info[1][5][2], dictionary_of_image_IDs[enemy_piece_info[1][5][3]]), Knight(window, enemy_piece_info[1][6][0], enemy_piece_info[1][6][1], enemy_piece_info[1][6][2], dictionary_of_image_IDs[enemy_piece_info[1][6][3]]), Rook(window, enemy_piece_info[1][7][0], enemy_piece_info[1][7][1], enemy_piece_info[1][7][2], dictionary_of_image_IDs[enemy_piece_info[1][7][3]]), Pawn(window, enemy_piece_info[1][8][0], enemy_piece_info[1][8][1], enemy_piece_info[1][8][2], dictionary_of_image_IDs[enemy_piece_info[1][8][3]]), Pawn(window, enemy_piece_info[1][9][0], enemy_piece_info[1][9][1], enemy_piece_info[1][9][2], dictionary_of_image_IDs[enemy_piece_info[1][9][3]]), Pawn(window, enemy_piece_info[1][10][0], enemy_piece_info[1][10][1], enemy_piece_info[1][10][2], dictionary_of_image_IDs[enemy_piece_info[1][10][3]]), Pawn(window, enemy_piece_info[1][11][0], enemy_piece_info[1][11][1], enemy_piece_info[1][11][2], dictionary_of_image_IDs[enemy_piece_info[1][11][3]]), Pawn(window, enemy_piece_info[1][12][0], enemy_piece_info[1][12][1], enemy_piece_info[1][12][2], dictionary_of_image_IDs[enemy_piece_info[1][12][3]]), Pawn(window, enemy_piece_info[1][13][0], enemy_piece_info[1][13][1], enemy_piece_info[1][13][2], dictionary_of_image_IDs[enemy_piece_info[1][13][3]]), Pawn(window, enemy_piece_info[1][14][0], enemy_piece_info[1][14][1], enemy_piece_info[1][14][2], dictionary_of_image_IDs[enemy_piece_info[1][14][3]]), Pawn(window, enemy_piece_info[1][15][0], enemy_piece_info[1][15][1], enemy_piece_info[1][15][2], dictionary_of_image_IDs[enemy_piece_info[1][15][3]])]

chess_pieces = [local, enemy]  # Keeps track of all the chess pieces

clock = pygame.time.Clock()

run = True
run_this = False  # Used to determine if the program should redraw stars
# Game Starts Here #
while run:
    clock.tick(100)

    player_can_move = False

    if local_piece_info[0] == 1:
        flip_coordinates(local_piece_info[1])

    enemy_piece_info = n.send_and_receive(local_piece_info)

    if local_piece_info[0] == 1:  # If player is black
        flip_coordinates(local_piece_info[1])
        flip_coordinates(enemy_piece_info[1])

    # Update enemy piece position #
    for i, enemy_piece in enumerate(chess_pieces[1]):
        enemy_piece.x = enemy_piece_info[1][i][0]
        enemy_piece.y = enemy_piece_info[1][i][1]
        enemy_piece.reDraw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    m1, m2, m3 = pygame.mouse.get_pressed()

    if m1:  # When the left mouse button is pressed
        m_pos = pygame.mouse.get_pos()  # Returns a tuple with x and y coordinates of mouse

        local_pos, enemy_pos = get_board_state(local_piece_info[1], enemy_piece_info[1])  # Get the positions of every piece
        for piece in chess_pieces[0]:  # Finds the piece that the player clicked on
            if piece.x <= m_pos[0] < piece.x + 60 and piece.y <= m_pos[1] < piece.y + 60:  # If the player clicked on a piece
                local_player.legal_moves = []  # Reset the legal moves of player
                local_player.selected_piece = piece  # Set the selected piece to this piece
                run_this = True
                resetBoard(ChessBoard_li, chess_pieces)  # Blit the current board layout
                piece.legal_moves = []  # Clears the list
                piece.getLegalMoves(local_pos, enemy_pos)  # Returns a list of coordinates to display
                local_player.legal_moves = piece.legal_moves  # Set the legal moves of the player to the legal moves of piece
                draw_stars(piece.legal_moves)  # Draw a star on every square the player can legally go to
                run_this = True
                break

        # Determine if player can move #
        if local_piece_info[0] == 0:  # If player is white
            if local_piece_info[2] == enemy_piece_info[2]:  # If white made the same number of moves as black
                player_can_move = True
        else:  # Player is black
            if local_piece_info[2] < enemy_piece_info[2]:  # If black made the same number of moves as white
                player_can_move = True

        # Move the selected piece #
        if player_can_move:
            for move in local_player.legal_moves:
                if move[0] <= m_pos[0] < move[0] + 60 and move[1] <= m_pos[1] < move[1] + 60:  # When player selected square to go to
                    local_piece_info[2] += 1
                    local_player.selected_piece.x = move[0]  # Set the x-coordinate of the selected piece to the selected square
                    local_player.selected_piece.y = move[1]  # Set the y-coordinate of the selected piece to the selected square
                    # Update local piece info #
                    for index in local_piece_info[1]:
                        if local_player.selected_piece.id == index[2]:
                            index[0] = local_player.selected_piece.x
                            index[1] = local_player.selected_piece.y
                            run_this = False
                            break
                    break

    reDraw_window(ChessBoard_li, chess_pieces[0], chess_pieces[1])

    if run_this:
        draw_stars(local_player.selected_piece.legal_moves)

    pygame.display.update()

pygame.quit()