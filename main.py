'''
Title: Chess
Author: John Yu
Date: 2019-03-03
'''

import math
from Classes import *
import pygame
from pygame.locals import *

def get_board_state(local, enemy):
    local_pieces = []  # Keeps track of the position of the player's pieces
    enemy_pieces = []  # Keeps track of the position of the enemy's pieces

    for i in range(len(local)):  # Local pieces
        local_pieces.append(local[i][:2])
    for i in range(len(enemy)):  # Enemy pieces
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

def piece_exists(info_list, piece_obj):
    for info_index in info_list:
        if info_index[2] == piece_obj.id:  # Compares id's
            return True  # When the piece object has been found
    return False

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

dictionary_of_player_turn = {
    0: 'WHITE',
    1: 'BLACK'
}

dictionary_of_player_move_text_colors = {
    0: (255, 255, 255),
    1: (0, 0, 0)
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
player_move_TEXT = pygame.font.SysFont('Bookman Old Style', 60)

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
process = 0  # Used to keep track of the number of times the program processed the entire while loop
previous_player_move = int(math.fabs(local_piece_info[2] - enemy_piece_info[2]))  # Used to help determine when player turn changes
change_in_turn = False
# Game Starts Here #
while run:
    clock.tick()

    player_move = int(math.fabs(local_piece_info[2] - enemy_piece_info[2]))  # Determines who's move it is. 0 is white's turn. 1 is black's turn.
    if not player_move == previous_player_move:  # When player turn changes
        change_in_turn = True
    # Display who's move it is #
        # Redraw text background #
    pygame.draw.rect(window, dictionary_of_player_move_text_colors[player_move], pygame.Rect(490, 5, 225, 70))
        # Redraw text #
    label = player_move_TEXT.render(dictionary_of_player_turn[player_move], 1, dictionary_of_player_move_text_colors[(player_move + 1) % 2])
    txt_size = player_move_TEXT.size(dictionary_of_player_turn[player_move])
    window.blit(label, (490 + ((225 - txt_size[0]) / 2), 5 + ((70 - txt_size[1]) / 2)))

    player_can_move = False  # Used to determine if the local player can move. Defaults to False

    if local_piece_info[0] == 1:
        flip_coordinates(local_piece_info[1])

    enemy_piece_info = n.send_and_receive(local_piece_info)

    if local_piece_info[0] == 1:  # If player is black
        flip_coordinates(local_piece_info[1])
        flip_coordinates(enemy_piece_info[1])

    # Update enemy piece position #
    for index, var in enumerate(chess_pieces[1]):  # For every enemy piece
        try:  # When it gets to the end of chess_pieces[1] and enemy_piece_info is out of range.
            if enemy_piece_info[1][index][2] == var.id:  # When ID's match up
                pass
            else:  # Means the piece got deleted from the database
                del chess_pieces[1][index]  # Delete the piece
                break
        except IndexError:
            del chess_pieces[1][index]  # Delete the variable
            break
        # Redraws every enemy piece
    for i, enemy_piece in enumerate(chess_pieces[1]):
        enemy_piece.x = enemy_piece_info[1][i][0]
        enemy_piece.y = enemy_piece_info[1][i][1]
        enemy_piece.reDraw(window)

    # Update local piece position #
    break_loop = False
    for counter, loc_pie in enumerate(chess_pieces[0]):  # loc_pie means local piece. I ran out of names to use.
        for en_pie in chess_pieces[1]:  # en_pie means enemy piece. I ran out of names to use.
            # The condition is true if the local piece shares a coordinate with an enemy piece and it is the local player's turn
            if loc_pie.x == en_pie.x and loc_pie.y == en_pie.y and player_move == local_piece_info[0]:
                del chess_pieces[0][counter]  # Delete the piece
                local_piece_info[1].pop(counter)  # Delete the piece specs from the local piece list
                change_in_turn = True
                break_loop = True
                break
        if break_loop:
            break
    # QUIT button #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    # Update legal moves of selected piece when enemy makes a move
    if change_in_turn:
        try:
            # Reset the legal moves of selected piece #
            local_pos, enemy_pos = get_board_state(local_piece_info[1], enemy_piece_info[1])  # Get the positions of every piece
            local_player.selected_piece.legal_moves = []  # Reset the legal moves of player
            reDraw_window(ChessBoard_li, chess_pieces[0], chess_pieces[1])
            if piece_exists(local_piece_info[1], local_player.selected_piece):  # Checks if the player's selected piece exists
                local_player.selected_piece.legal_moves = []  # Clears the list
                local_player.selected_piece.getLegalMoves(local_pos, enemy_pos)  # Returns a list of coordinates to display
                draw_stars(local_player.selected_piece.legal_moves)  # Draw a star on every square the player can legally go to
                change_in_turn = False
        except AttributeError:
            pass

    m1, m2, m3 = pygame.mouse.get_pressed()

    if m1 and process > 1:  # When the left mouse button is pressed
        # and the program has processed the while loop more than once.
        # This is to make sure stars are not drawn right when after player moves a piece.
        m_pos = pygame.mouse.get_pos()  # Returns a tuple with x and y coordinates of mouse

        local_pos, enemy_pos = get_board_state(local_piece_info[1], enemy_piece_info[1])  # Get the positions of every piece
        for piece in chess_pieces[0]:  # Finds the friendly piece that the player clicked on
            if piece.x <= m_pos[0] < piece.x + 60 and piece.y <= m_pos[1] < piece.y + 60:  # If the player clicked on a piece
                local_player.selected_piece = piece  # Set the selected piece to this piece
                run_this = True
                reDraw_window(ChessBoard_li, chess_pieces[0], chess_pieces[1])
                piece.legal_moves = []  # Clears the list
                piece.getLegalMoves(local_pos, enemy_pos)  # Returns a list of coordinates to display
                draw_stars(piece.legal_moves)  # Draw a star on every square the player can legally go to
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
            for move in local_player.selected_piece.legal_moves:
                if move[0] <= m_pos[0] < move[0] + 60 and move[1] <= m_pos[1] < move[1] + 60:  # When player selected square to go to
                    local_piece_info[2] += 1  # Add 1 to total moves made by local player
                    local_player.selected_piece.x = move[0]  # Set the x-coordinate of the selected piece to the selected square
                    local_player.selected_piece.y = move[1]  # Set the y-coordinate of the selected piece to the selected square
                    process = 0
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

    process += 1  # Program has ran through the entire while loop once

    pygame.display.update()

pygame.quit()