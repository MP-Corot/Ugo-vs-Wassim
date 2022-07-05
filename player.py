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

import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.hp = 100
        self.game = game
        self.max_hp = 100
        self.atk = 25
        self.speed = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("PygameAssets-main/ugo.png")
        self.image = pygame.transform.scale(self.image, (160, 160))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def taking_dmg(self, nb_dmg):
        if self.hp > nb_dmg:
            self.hp -= nb_dmg
        elif self.game.is_playing:
            self.game.game_over()

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def jump(self, t):
        ypos = 10 * (t**2) - 100 * t + 500
        if ypos > 500:
            self.rect.y = 500
        else:
            self.rect.y = ypos

    def launch_proj(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def update_hp_bar(self, surface):
        new_x = self.rect.x + 50
        new_y = self.rect.y + 20
        pygame.draw.rect(surface, (89, 96, 81), [new_x, new_y, self.max_hp, 8])
        pygame.draw.rect(surface, (140, 227, 35), [new_x, new_y, self.hp, 8])
