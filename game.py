import pygame
from game_surface import Surface

# Initalize module
pygame.init()

# Create surface
screen_width, screen_height = 500, 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sname Game")

# Create 3X3 grid
lines1 = Surface(150, 60, 30, 100, '#027559')

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
    screen.blit(screen, lines1.game_rects(screen))

    # Flip game
    pygame.display.flip()

    screen.fill('#08D1B0')
pygame.quit