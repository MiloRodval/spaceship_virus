import pygame

class Jank:

    def __init__(self, height, speed, position={'x_position': 0, 'y_position': 0}):
        self.height = height
        self.speed = speed
        self.position = position

    def scaled_bullet_image(self):
        return pygame.transform.scale(pygame.image.load('interface/images/laser_beam2.png').convert_alpha(), (60, self.height))
    
    def blit(self, screen):
        return screen.blit(self.scaled_bullet_image(), (self.position['x_position'], self.position['y_position']))

    def update(self, width, bullets):
        self.position['x_position'] += self.speed
        if self.position['x_position'] > width:
            bullets.remove(self)

    def take_life_from(self, thing):

        if type(thing.position) == int:
            if self.position == thing:
                thing.life =- 1

        elif type(thing.position) == list:
            for i in range(len(thing.position)):
                if self.position == thing.position[i]:
                    thing.life -= 1

    @classmethod
    def get(cls):
        return cls()
    
    @property
    def height(self):
        return self._height
    
    @property
    def position(self):
        return self._position
    
    @property
    def speed(self):
        return self._speed
    
    @height.setter
    def height(self, height):
        if height:
            self._height = height
    
    @position.setter
    def position(self, position):
        if position:
            self._position = position
        else:
            raise ValueError('Position variable is missing')

    @speed.setter
    def speed(self, speed):
        if speed:
            self._speed = speed
        else:
            raise ValueError('speed variable is missing')

