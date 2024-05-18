import pygame
# I can use this: pygame.display.get_window_size()
width = 1300

class Player_bullet(pygame.sprite.Sprite):
    def __init__(self, width, speed, position):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.speed = speed
        self.image = pygame.image.load('interface/images/laserbeam.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midleft = position

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > self.width:
            self.kill()

class Enemy_bullet(pygame.sprite.Sprite):
    def __init__(self, speed, position):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.image.load('interface/images/laserbeam.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midright = position

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right <= 0:
            self.kill()