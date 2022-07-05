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
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.hp = 100
        self.max_hp = 100
        self.atk = 0.1
        self.velocity = random.randint(1, 2)
        self.image = pygame.image.load('PygameAssets-main/wassim.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 950 + random.randint(0, 200)
        self.rect.y = 550
        self.game = game

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            if random.random() > 0.2:
                self.rect.x -= self.velocity
        else:
            self.game.player.taking_dmg(self.atk)

        if self.rect.x < 0:
            self.rect.x = random.randint(1000, 1300)

    def taking_dmg(self, nb_dmg):
        self.hp -= nb_dmg
        if self.hp <= 0:
            self.rect.x = 1000 + random.randint(0, 200)
            self.hp = self.max_hp
            self.velocity = random.randint(1, 2)
            self.game.score += 1
            self.game.bossBar_percent += 2

    def update_hp_bar(self, surface):
        new_x = self.rect.x + 10
        new_y = self.rect.y - 5
        pygame.draw.rect(surface, (89, 96, 81), [new_x, new_y, self.max_hp, 5])
        pygame.draw.rect(surface, (140, 227, 35), [new_x, new_y, self.hp, 5])
