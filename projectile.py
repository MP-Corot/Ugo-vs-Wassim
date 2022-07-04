import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.speed = 2
        self.dmg = player.atk
        self.player = player
        self.image = pygame.image.load("PygameAssets-main/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def move(self):
        self.rect.x += self.speed
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            monster.taking_dmg(self.player.atk)
            self.remove()

        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
