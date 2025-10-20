# If mouse collids with any of the areas inside the function that change colors
import pygame
from game_surface import Surface

pygame.init()

class gridArea:
    def Areas():
        # Top Row
        area1 = Surface(150, 60, 50, 50, '#08D1B0')
        area2 = Surface(211, 60, 50, 50, '#08D1B0')
        area3 = Surface(273, 60, 50, 50, '#08D1B0')

        # Mid Row
        area4 = Surface(150, 121, 50, 50, '#08D1B0')
        area5 = Surface(211, 121, 50, 50, '#08D1B0')
        area6 = Surface(273, 121, 50, 50, '#08D1B0')

        # Bottom Row
        area7 = Surface(150, 183, 50, 50, '#08D1B0')
        area8 = Surface(211, 183, 50, 50, '#08D1B0')
        area9 = Surface(273, 183, 50, 50, '#08D1B0')


        playerPosition = [area1, area2, area3, area4, area5, area6, area7, area8, area9]
        return playerPosition