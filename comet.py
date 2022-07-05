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

import random

import pygame


class Comet(pygame.sprite.Sprite):

    def __init__(self, game):
        super(Comet, self).__init__()
        self.dmg = 0.3
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/benalia.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.y = -10
        self.rect.x = random.randint(0, 900)
        self.game = game

    def move_bot(self):

        if self.game.check_collision(self, self.game.all_players):
            self.game.player.taking_dmg(self.dmg)
            self.game.all_comets.remove()

        elif self.rect.y > 900:
            self.rect.y = -10
            self.rect.x = random.randint(0, 700)
            self.velocity = random.randint(1,2)

        else:
            self.rect.y += self.velocity
