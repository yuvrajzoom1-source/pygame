import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Event")

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
    def change_color(self):
        self.image.fill(random.choice(colors))

sprite1 = Box(150, 200, colors[0])
sprite2 = Box(350, 200, colors[1])
all