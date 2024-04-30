import pygame

class Jank:

    def __init__(self, box, position, velocity):
        self.box = box
        self.position = position
        self.velocity = velocity

    def scaled_bullet_image(self):
        return pygame.transform.scale(pygame.image.load('interface/images/laser_beam2.png').convert_alpha(), (self.box, 60))
    
    def blit(self, screen):
        return screen.blit(self.scaled_bullet_image(), self.position)

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
    def box(self):
        return self._box
    
    @property
    def position(self):
        return self._position
    
    @property
    def velocity(self):
        return self._velocity
    
    @box.setter
    def box(self, box):
        if box:
            self._box = box
    
    @position.setter
    def position(self, position):
        if position:
            self._position = position
        else:
            raise ValueError('Position variable is missing')

    @velocity.setter
    def velocity(self, velocity):
        if velocity:
            self._velocity = velocity
        else:
            raise ValueError('Velocity variable is missing')

