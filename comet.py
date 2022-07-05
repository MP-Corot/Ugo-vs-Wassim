import random

import pygame


class Comet(pygame.sprite.Sprite):

    def __init__(self, game):
        super(Comet, self).__init__()

        self.dmg = 0.3
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.y = -10
        self.rect.x = random.randint(0, 900)
        self.game = game

    def move_bot(self):

        if self.game.check_collision(self, self.game.all_player):
            self.game.player.taking_dmg(self.dmg)
            self.game.all_comet.remove()

        elif self.rect.y > 900:
            self.rect.y = -10
            self.rect.x = random.randint(0, 1000)

        else:
            self.rect.y += self.velocity
