'''
Title: Chess
Author: John Yu
Date: 2019-03-03
'''

import pygame
import math

pygame.init() # Initialize Pygame

windowx = 480
windowy = 480
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
    ### --- Create the ChessBoard --- ###
ChessBoard = []
ChessBoardColors = [(255, 248, 220), (139, 69, 19)] # Colors: Cornsilk, Saddlebrown
for i in range(64):
    x = (i % 8) * 60
    column = (i % 8)
    y = math.floor(i / 8) * 60
    row = math.floor(i / 8)
    ChessBoard.append(Squares(window, x, y, ChessBoardColors[(column + row) % 2]))

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.update()

pygame.quit()