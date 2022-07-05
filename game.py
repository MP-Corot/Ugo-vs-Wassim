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

from player import Player
from monster import Monster
from comet import Comet


class Game:

    def __init__(self):

        # joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}

        self.is_playing = False
        self.score = 0
        self.all_monsters = pygame.sprite.Group()
        self.all_comets = pygame.sprite.Group()
        self.bossBar_percent = 0

    def update_bar(self, surface):

        # arrière plan
        pygame.draw.rect(surface,(0,0,0),[0,surface.get_height()-10,surface.get_width(),10])
        # bar
        pygame.draw.rect(surface,(53, 157, 209),[0,surface.get_height()-10,surface.get_width()*self.bossBar_percent/100,10])

    def summon_commet(self):
        self.commet = Comet(self)
        self.all_comets.add(self.commet)

    def summon_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def movement(self, t):

        if self.pressed.get(pygame.K_q) and self.player.rect.x > -50:
            self.player.move_left()
        if self.pressed.get(pygame.K_d) and self.player.rect.x < 930:
            self.player.move_right()
        if self.pressed.get(pygame.K_z) or self.player.rect.y != 500:
            self.player.jump(t)
            t += 0.03
        return t

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        self.player.hp = self.player.max_hp
        self.player.rect.x = 200
        self.is_playing = False
        self.all_monsters = pygame.sprite.Group()
        self.all_comets = pygame.sprite.Group()
        self.pressed = {}
        self.bossBar_percent = 0
        print(self.score)
        self.score = 0

    def start(self):
        self.is_playing = True

        self.summon_monster()
        self.summon_monster()
        self.summon_monster()

        self.summon_commet()
        self.summon_commet()

    def update(self, surface, img):

        surface.blit(img, (0, -200))

        surface.blit(self.player.image, self.player.rect)
        self.player.update_hp_bar(surface)
        self.update_bar(surface)

        # projectile

        self.player.all_projectiles.draw(surface)
        for projectile in self.player.all_projectiles:
            projectile.move()

        # monster
        self.all_monsters.draw(surface)
        for monster_el in self.all_monsters:
            monster_el.forward()
            monster_el.update_hp_bar(surface)

        # comet

        self.all_comets.draw(surface)
        for comet in self.all_comets:
            comet.move_bot()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    self.player.launch_proj()

            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
