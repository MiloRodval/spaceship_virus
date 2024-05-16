import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('interface/images/enemy_ship.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)