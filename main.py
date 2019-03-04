'''
Title: Chess
Author: John Yu
Date: 2019-03-03
'''

import pygame
import math

pygame.init() # Initialize Pygame

windowx = 720
windowy = 600
window = pygame.display.set_mode((windowx, windowy)) # Creates the window
pygame.display.set_caption('Chess')

class Squares():
    def __init__(self, window, x, y, color):
        self.x = x
        self.y = y
        self.color = color

        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, 60, 60))

clock = pygame.time.Clock()

### --- Code Starts Here --- ###
window.fill((200, 200, 200)) # Create Background
    ### --- Create the ChessBoard --- ###
ChessBoard = []
ChessBoardColors = [(255, 222, 173), (139, 69, 19)] # Colors: Navajowhite, Saddlebrown
for i in range(64):
    x = (i % 8) * 60
    column = (i % 8)
    y = (math.floor(i / 8) * 60) + 60
    row = math.floor(i / 8)
    ChessBoard.append(Squares(window, x, y, ChessBoardColors[(column + row) % 2]))

    ### --- Create Control Panel --- ###
        ### --- Background --- ###
pygame.draw.rect(window, (255, 255, 255), pygame.Rect(485, 0, 235, 600))

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.update()

pygame.quit()