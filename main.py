import pygame
import importlib.util
import sys
import os
spec = importlib.util.spec_from_file_location("mygame", os.path.join(os.path.dirname(__file__), "game.py"))
game = importlib.util.module_from_spec(spec)
sys.modules["mygame"] = game
spec.loader.exec_module(game)

pygame.init()
screen = pygame.display.set_mode((960,540))
pygame.display.set_caption("Garden Defender")
pozadi = pygame.image.load("herniPozadi.png").convert()
logo = pygame.image.load("logo.png").convert_alpha()
start_button = pygame.image.load("start.png").convert_alpha()

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # start button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                game.game_window() 

    # pozadí
    screen.blit(pozadi, (0, 0))
    # logo
    #logo má 533px na šířku, proto vykresleno na 213px (960-533)/2
    screen.blit(logo, (213, 20))
    #  tlačítko start
    start_rect = start_button.get_rect(center=(960 // 2, 300))
    screen.blit(start_button, start_rect)

    pygame.display.update()

pygame.quit()