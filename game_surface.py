import pygame

class Surface:
    def __init__(self, x_pos, y_pos, width, height, color):
        pygame.init()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.draw_rects = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.active = False
    
    def game_rects(self, screen):
        # draw_rects = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        return pygame.draw.rect(screen, self.color, self.draw_rects)

    def on_click(self):
        self.active = True

    def selection(self, screen):
        pygame.draw.rect(screen, self.color, self.draw_rects)
        if self.active:
            highlight_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
            pygame.draw.rect(screen, 'green', highlight_rect)

    
    # def check_hover(self, mouse):
    #     if self.draw_rects.collidepoint(mouse):
    #         self.color = 'green'  # Hover color
    #     else:
    #         self.color = '#08D1B0'