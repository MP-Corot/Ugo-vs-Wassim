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
        self.image = pygame.image.load('PygameAssets-main/ugo.png')
        self.image = pygame.transform.scale(self.image,(160,160))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def taking_dmg(self, nb_dmg):
        if self.hp - nb_dmg > 0:
            self.hp -= nb_dmg
        elif self.game.is_playing:
            self.game.game_over()

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def jump(self, t):
        ypos = 10 * (t ** 2) - 100 * t + 500
        if ypos > 500:
            self.rect.y = 500
        else:
            self.rect.y = ypos

    def launch_proj(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def update_hp_bar(self, surface):
        pygame.draw.rect(surface, (89, 96, 81), [self.rect.x + 50, self.rect.y + 20, self.max_hp, 8])
        pygame.draw.rect(surface, (140, 227, 35), [self.rect.x + 50, self.rect.y + 20, self.hp, 8])
