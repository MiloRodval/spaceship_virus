import pygame

class Spaceship(World):
    def __init__(self, x_position, y_position, box):
        self.x_position = x_position
        self.y_position = y_position
        self.life = 3
        self.spaceship_source = 'interface/images/spaceship.png'
        # Cambiar a center despues
        self.box = box
        self.speed = self.box

    @property
    def y_position(self):
        return self._y_position
    
    @y_position.setter
    def y_position(self, y_position):
        if 0 < y_position < self.height:
            self._y_position = y_position


    @classmethod
    def get(cls):
        return cls()

class Enemy(Spaceship):
    def __init__(self, x_position, y_position, box):
        super().__init__(x_position, y_position, box)
        self.x_position = x_position
        self.y_position = y_position
        self.spaceship_source = 'interface/images/enemy_ship.png'
        self.box = box