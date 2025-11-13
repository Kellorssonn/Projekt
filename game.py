import pygame
import random
import time
import main  # kvůli návratu do menu
from player import Player
from enemy import Enemy

def game_window():
    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Garden Defender")

    pozadi = pygame.image.load("herniPozadi.png").convert()

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 48)

    player = Player(100, 270)
    enemies = []
    score = 0

    spawn_time = time.time() + random.uniform(0.2, 1)

    running = True
    game_over = False
    game_over_time = 0

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player.shoot()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    player.shoot()

        keys = pygame.key.get_pressed()
        if not game_over:
            player.move(keys)

        # Spawn nového enemy po uplynutí intervalu
        if not game_over and time.time() >= spawn_time:
            enemies.append(Enemy())
            spawn_time = time.time() + random.uniform(0.2, 1)

        # vykreslení pozadí
        screen.blit(pozadi, (0, 0))

        if not game_over:
            player.update(screen)

            # pohyb a vykreslení nepřátel
            for enemy in enemies[:]:
                enemy.move()
                enemy.draw(screen)

                # kolize s hráčem
                if enemy.rect.colliderect(player.rect):
                    game_over = True
                    game_over_time = time.time()

                # kolize se střelou
                for projectile in player.projectiles[:]:
                    if enemy.rect.colliderect(projectile.rect):
                        enemies.remove(enemy)
                        player.projectiles.remove(projectile)
                        score += 1
                        break

                # pokud dojde na levou stranu → konec hry
                if enemy.rect.left <= 0:
                    game_over = True
                    game_over_time = time.time()

            # vykreslení skóre
            score_text = font.render(str(score), True, (255, 255, 255))
            screen.blit(score_text, (900, 10))

        else:
            # GAME OVER nápis
            over_text = font.render("GAME OVER", True, (255, 50, 50))
            text_rect = over_text.get_rect(center=(480, 270))
            screen.blit(over_text, text_rect)

            # po 5 vteřinách návrat do menu
            if time.time() - game_over_time >= 5:
                running = False
                pygame.quit()
                main.__name__ == "__main__" and __import__("main")

        pygame.display.update()
