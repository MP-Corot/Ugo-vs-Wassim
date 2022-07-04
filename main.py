"""
MIT License

Copyright (c) 2022 MP-Corot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import math

import pygame
from game import Game

pygame.init()

if __name__ == '__main__':
    game = Game()
    # fenetre
    pygame.display.set_caption("Wassim VS Ugo")
    screen = pygame.display.set_mode((1080, 720))

    # arrière plan
    bg = pygame.image.load('PygameAssets-main/bg.jpg')
    screen.blit(bg, (0, -200))
    banner = pygame.image.load("PygameAssets-main/banner.png")
    banner = pygame.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)

    # button
    button = pygame.image.load("PygameAssets-main/button.png")
    button = pygame.transform.scale(button, (400, 150))
    button_rect = button.get_rect()
    button_rect.x = math.ceil(screen.get_width() / 3.33)
    button_rect.y = math.ceil(screen.get_height() / 2)

    # variable
    running = True
    t = 0
    time_btw_jump = 11

    # spawn
    # boucle principale
    while running:
        # player
        pygame.display.flip()
        if game.is_playing:
            t = game.movement(t)
            if t >= time_btw_jump:
                t = 0
            game.update(screen, bg)

        else:
            screen.blit(button, (banner_rect.x + 60, 400))
            screen.blit(banner, (banner_rect.x, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                    game.start()
