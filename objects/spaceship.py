import pygame

class Spaceship:
    def __init__(self, speed, height, enemy, position={'x_position': 0, 'y_position': 0}, life=3):
        self.speed = speed
        self.height = height
        self.enemy = enemy
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
        return pygame.transform.scale(pygame.image.load(self.get_path()).convert_alpha(), (self.height, 70))

    def move_down(self):
        new_position = self.position.copy()
        new_position['y_position'] += self.speed
        self.position = new_position

    def move_up(self):
        new_position = self.position.copy()
        new_position['y_position'] -= self.speed
        self.position = new_position

    def shoot(self):
        '''position_copy = self.position.copy()
        shooting = True
        while shooting:
            pygame.transform.scale(
                pygame.image.load('interface/images/laser_beam2.png').convert_alpha(),
                (position_copy['x_position'], position_copy['y_position']/2)
            )
            if self.enemy == True:
                position_copy['y_position'] =- self.speed
                if position_copy['y_position'] < 0:
                    self.enemy = False
            elif self.enemy == False:
                position_copy['y_position'] =+ self.speed
                if position_copy['y_position'] > 1300:
                    self.enemy = True'''

    def die(self):
        print('YOU ARE DEAD')

    @property
    def speed(self):
        return self._speed

    @property
    def height(self):
        return self._height

    @property
    def enemy(self):
        return self._enemy

    @property
    def position(self):
        return self._position
    
    @property
    def life(self):
        return self._life

    @speed.setter
    def speed(self, speed):
        if speed:
            self._speed = speed
        else:
            raise ValueError('Speed variable missing')
        
    @height.setter
    def height (self, height):
        if height:
            self._height = height

    @enemy.setter
    def enemy(self, enemy):
        self._enemy = enemy

    @position.setter
    def position(self, new_position):
        # Raro. Deberia ser * 10 - 1 (restando la height de la spaceship)
        if self.height - self.height <= new_position['y_position'] <= self.height * 8:
            self._position = new_position
            
    @life.setter
    def life(self, life):
        if life:
            self._life = life
        elif life == 0:
            self.die()
        else:
            raise ValueError('Life variable missing')
    