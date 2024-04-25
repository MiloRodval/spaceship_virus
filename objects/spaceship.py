import pygame

class Spaceship:
    def __init__(self, speed, position={'x_position': 0, 'y_position': 0}, life=3):
        self.speed = speed
        self.position = position
        self.life = life

    def __str__(self):
        return f'{self.position = }'
    
    @classmethod
    def get(cls):
        return cls()
    
    def get_path(self):
        return 'interface/images/spaceship.png'

    def scaled_spaceship_image(self):
        return pygame.transform.scale(pygame.image.load(self.get_path()).convert_alpha(), (100, 150))

    def move_down(self):
        new_position = self.position.copy()
        new_position['y_position'] += self.speed
        self.position = new_position

    def move_up(self):
        new_position = self.position.copy()
        new_position['y_position'] -= self.speed
        self.position = new_position

    def die(self):
        print('YOU ARE DEAD')

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        if speed:
            self._speed = speed
        else:
            raise ValueError('Speed variable missing')

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if -50 <= new_position['y_position'] <= 300:
            self._position = new_position
        
    @property
    def life(self):
        return self._life
    
    @life.setter
    def life(self, life):
        if life:
            self._life = life
        elif life == 0:
            self.die()
        else:
            raise ValueError('Life variable missing')