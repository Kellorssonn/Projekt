import pygame
from projectile import Projectile
import time

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed = 5
        self.projectiles = []
        self.last_shot_time = 0  # čas posledního výstřelu
        self.shoot_cooldown = 0.6  # sekundy

    def move(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 540:
            self.rect.bottom = 540

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            projectile = Projectile(self.rect.right, self.rect.centery)
            self.projectiles.append(projectile)
            self.last_shot_time = current_time

    def update(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        for projectile in self.projectiles[:]:
            projectile.move()
            projectile.draw(screen)
            if projectile.rect.left > 960:
                self.projectiles.remove(projectile)
