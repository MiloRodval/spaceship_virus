class Spaceship:
    def __init__(self, position=[0, 1, 2], life=3):
        self.position = position
        self.life = life

    def __str__(self):
        return f'{self.position = }'
    
    @classmethod
    def get(cls):
        return cls()

    def move_down(self):
        self.position[0] += 1
        self.position[1] += 1
        self.position[2] += 1

    def move_up(self):
        self.position[0] -= 1
        self.position[1] -= 1
        self.position[2] -= 1

    def shoot(self, jank):
        jank.bullet(self.position[1], 'left_to_right')

    def die(self):
        print('YOU ARE DEAD')

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if position:
            self._position = position
        else:
            raise ValueError('Position variable missing')
        
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