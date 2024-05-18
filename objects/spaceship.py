import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('interface/images/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = speed