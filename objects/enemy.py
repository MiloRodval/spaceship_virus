import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, speed, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('interface/images/enemy_ship.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = speed
        self.height = height

    def update(self):
        if self.rect.top >= 0 or self.rect.bottom <= self.height:
            self.rect.move_ip(0, self.speed)
    
    def killed(self):
        self.kill()