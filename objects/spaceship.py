import pygame

class Spaceship:
    def __init__(self, x_position, y_position, box):
        self.x_position = x_position
        self.y_position = y_position
        self.life = 3
        self.spaceship_source = 'interface/images/spaceship.png'
        # Cambiar a center despues
        self.box = box
        self.speed = self.box

    @classmethod
    def get(cls):
        return cls()

    def move_down(self):
        new_position = self.rect.copy()
        new_position.bottom += self.speed
        # Only moves if it doesn't go lower that the last box of the gaming screen
        if new_position.bottom < self.box*12:
            self.bottom = new_position

    def move_up(self):
        new_position = self.rect.copy()
        new_position.top -= self.speed
        # Only moves if it doesn't go beyond the top of the screen
        if new_position.top > self.box-self.box:
            self.top = new_position

class Enemy(Spaceship):
    def __init__(self, x_position, y_position, box):
        super().__init__(x_position, y_position, box)
        self.x_position = x_position
        self.y_position = y_position
        self.spaceship_source = 'interface/images/ship.png'
        self.box = box