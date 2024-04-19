class Spaceship:
    def __init__(self, position=[0, 1, 2]):
        self.position = position

    def __str__(self):
        return f'{self.position = }'
    
    @classmethod
    def get(cls):
        return cls()

    def move_up(self):
        self.position[0] += 1
        self.position[1] += 1
        self.position[2] += 1

    def move_down(self):
        self.position[0] -= 1
        self.position[1] -= 1
        self.position[2] -= 1

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position