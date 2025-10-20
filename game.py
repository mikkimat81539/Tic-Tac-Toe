import pygame
from game_surface import Surface

# Initalize module
pygame.init()

# Create surface
screen_width, screen_height = 500, 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sname Game")

# Create 3X3 grid
vert1 = Surface(200, 60, 10, 175, '#027559')
vert2 = Surface(262, 60, 10, 175, '#027559')

hort1 = Surface(150, 110, 174, 10, '#027559')
hort2 = Surface(150, 172, 174, 10, '#027559')

# Create boundaries

# Top Row
area1 = Surface(150, 60, 50, 50, 'white')
area2 = Surface(211, 60, 50, 50, 'white')
area3 = Surface(273, 60, 50, 50, 'white')

# Mid Row
area4 = Surface(150, 121, 50, 50, 'white')
area5 = Surface(211, 121, 50, 50, 'white')
area6 = Surface(273, 121, 50, 50, 'white')

# Bottom Row
area7 = Surface(150, 183, 50, 50, 'white')
area8 = Surface(211, 183, 50, 50, 'white')
area9 = Surface(273, 183, 50, 50, 'white')


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

    # Draw Game Board
    vert1.game_rects(screen)
    vert2.game_rects(screen)

    hort1.game_rects(screen)
    hort2.game_rects(screen)

    # Define area
    area1.game_rects(screen)
    area2.game_rects(screen)
    area3.game_rects(screen)
    area4.game_rects(screen)
    area5.game_rects(screen)
    area6.game_rects(screen)
    area7.game_rects(screen)
    area8.game_rects(screen)
    area9.game_rects(screen)

    # Flip game
    pygame.display.flip()

    screen.fill('#08D1B0')
pygame.quit