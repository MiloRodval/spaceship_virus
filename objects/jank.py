class Jank:
    '''
    "Jank" include everything that moves through space from left to right or right to left and takes lifes.
    That means that a bullet from a spaceship is also "junk".
    '''
    def __init__(self, position: int, velocity: float, direction: str):
        self.position = position
        self.velocity = velocity
        self.direction = direction
    
    def __str__(self):
        f'{self.position = }{self.velocity = }{self.direction = }'


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
    def position(self):
        return self._position
    
    @property
    def velocity(self):
        return self._velocity
    
    @property
    def direction(self):
        return self._direction
    
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

    @direction.setter
    def direction(self, direction):
        if direction:
            self._direction = direction
        else:
            raise ValueError('Direction variable is missing')

