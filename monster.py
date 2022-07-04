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
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 950 + random.randint(0, 200)
        self.rect.y = 550
        self.game = game

    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
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


    def update_hp_bar(self, surface):
        pygame.draw.rect(surface, (89, 96, 81), [self.rect.x + 10, self.rect.y - 5, self.max_hp, 5])
        pygame.draw.rect(surface, (140, 227, 35), [self.rect.x + 10, self.rect.y - 5, self.hp, 5])
