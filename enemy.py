import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("sunflower.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 960  # začne úplně na pravém okraji
        self.rect.y = random.randint(0, 540 - 40)  # náhodná vertikální pozice
        self.speed = 3

    def move(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
