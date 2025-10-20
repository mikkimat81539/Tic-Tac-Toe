import pygame
from game_surface import Surface

# Initalize module
pygame.init()

# Create surface
screen_width, screen_height = 500, 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sname Game")

# Create 3X3 grid
vert1 = Surface(200, 60, 10, 200, '#027559')
vert2 = Surface(290, 60, 10, 200, '#027559')

hort1 = Surface(150, 110, 200, 10, '#027559')
hort2 = Surface(150, 190, 200, 10, '#027559')

# Create player (X)


# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)

        if event.type == pygame.QUIT:
            running = False

    # Render Game Here
    vert1.game_rects(screen)
    vert2.game_rects(screen)

    hort1.game_rects(screen)
    hort2.game_rects(screen)

    # Flip game
    pygame.display.flip()

    screen.fill('#08D1B0')
pygame.quit