import pygame

class Surface:
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        pygame.init()
    
    def game_rects(self, screen):
        draw_rects = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        return pygame.draw.rect(screen, self.color, draw_rects)