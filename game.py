from objects.spaceship import Spaceship
from objects.jank import Jank

def main():
    my_spaceship = Spaceship()
    my_spaceship.move_down()
    my_spaceship.move_down()
    my_spaceship.move_down()
    my_spaceship.move_down()
    enemy_bullet = Jank(5, 0.5, 'left_to_right')
    if enemy_bullet.position in my_spaceship.position:
        enemy_bullet.take_life_from(my_spaceship)
        enemy_bullet.take_life_from(my_spaceship)
        enemy_bullet.take_life_from(my_spaceship)

if __name__ == "__main__":
    main()