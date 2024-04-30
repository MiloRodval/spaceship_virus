import pygame

class Spaceship:
    def __init__(self, speed, height, position={'x_position': 0, 'y_position': 0}, life=3):
        self.speed = speed
        self.height = height
        self.position = position
        self.life = life
        #self.mask = pygame.mask.from_surface(self.scaled_spaceship_image())

    def __str__(self):
        return f'{self.position = }'

    @classmethod
    def get(cls):
        return cls()

    def get_path(self):
        return 'interface/images/spaceship.png'

    def scaled_spaceship_image(self):
        return pygame.transform.scale(pygame.image.load(self.get_path()).convert_alpha(), (60, self.height))
    
    def blit(self, screen):
        return screen.blit(self.scaled_spaceship_image(), (self.position['x_position'], self.position['y_position']))

    def move_down(self):
        new_position = self.position.copy()
        new_position['y_position'] += self.speed
        self.position = new_position

    def move_up(self):
        new_position = self.position.copy()
        new_position['y_position'] -= self.speed
        self.position = new_position

    def shoot(self):
        position_copy = self.position.copy()
        shooting = True
        while shooting:
            pygame.transform.scale(
                pygame.image.load('interface/images/laser_beam2.png').convert_alpha(),
                (position_copy['x_position'] + 50, position_copy['y_position']/2)
            )
            shooting = False

    def die(self):
        print('YOU ARE DEAD')

    @property
    def speed(self):
        return self._speed

    @property
    def height(self):
        return self._height

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

    @position.setter
    def position(self, new_position):
        if 0 <= new_position['y_position'] <= (10 - 1) * self.height:
            self._position = new_position
            
    @life.setter
    def life(self, life):
        if life:
            self._life = life
        elif life == 0:
            self.die()
        else:
            raise ValueError('Life variable missing')
    
class Enemy(Spaceship):
    def __init__(self, speed, height, position={'x_position': 0, 'y_position': 0}, life=1):
        super().__init__(speed, height, position={'x_position': 0, 'y_position': 0}, life=1)
        self.speed = speed
        self.height = height
        self.position = position
        self.life = life

    def get_path(self):
        return 'interface/images/ExportedLayers.png'

    def scaled_spaceship_image(self):
        return pygame.transform.scale(pygame.image.load(self.get_path()).convert_alpha(), (60, self.height))
    
    def blit(self, screen):
        return screen.blit(self.scaled_spaceship_image(), (self.position['x_position'], self.position['y_position']))
