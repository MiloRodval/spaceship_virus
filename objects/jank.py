class Jank:
    def __init__(self, position: int, velocity: float, direction: str):
        self.position = position
        self.velocity = velocity
        self.direction = direction
    
    def __str__(self):
        f'{self.position = }{self.velocity = }{self.direction = }'

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
        self._position = position

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    @direction.setter
    def direction(self, direction):
        self._direction = direction