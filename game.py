import pygame
from game_surface import Surface
from boundaries import gridArea

# Initalize module
pygame.init()

# Create surface
screen_width, screen_height = 500, 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

# Create 3X3 grid
vert1 = Surface(200, 60, 10, 175, '#027559')
vert2 = Surface(262, 60, 10, 175, '#027559')

hort1 = Surface(150, 110, 174, 10, '#027559')
hort2 = Surface(150, 172, 174, 10, '#027559')

# Define Area
grid_area = gridArea.Areas()

# Game loop
running = True

while running:
    for event in pygame.event.get():
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse = pygame.mouse.get_pos()
        #     print(mouse)

        if event.type == pygame.QUIT:
            running = False

    # Render Game Here

    # Draw Game Board
    vert1.game_rects(screen)
    vert2.game_rects(screen)

    hort1.game_rects(screen)
    hort2.game_rects(screen)

    # Update and draw areas
    mouseDetect = pygame.mouse.get_pos()

    for area in grid_area:
        area.check_hover(mouseDetect)
        area.game_rects(screen)

    # Flip game
    pygame.display.flip()

    screen.fill('#08D1B0')
pygame.quit