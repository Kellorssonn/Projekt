import pygame

class Projectile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y - 5, 10, 10)
        self.speed = 10

    def move(self):
        self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), self.rect.center, 5)
