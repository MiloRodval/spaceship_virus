import pygame

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.box = round(self.height / 13)
    

class Screen(World):
    def __init__(self, background_image_source):
        self.background_image_source = background_image_source
    

class Spaceship(World):
    def __init__(self, x_position, y_position, width, height):
        super().__init__(width, height)
        self.x_position = x_position
        self.y_position = y_position
        self.life = 3
        self.spaceship_source = 'interface/images/spaceship.png'
        self.width = width
        self.height = height
        self.box = round(self.height / 13)
        self.speed = self.box

    @property
    def y_position(self):
        return self._y_position
    
    @y_position.setter
    def y_position(self, y_position):
        if self.box < y_position < self.height-self.box:
            self._y_position = y_position

    @classmethod
    def get(cls):
        return cls()

class Enemy(Spaceship):
    def __init__(self, x_position, y_position, width, height):
        super().__init__(x_position, y_position, width, height)
        self.x_position = x_position
        self.y_position = y_position
        self.spaceship_source = 'interface/images/enemy_ship.png'
        self.width = width
        self.height = height
