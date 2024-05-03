from objects.spaceship import Spaceship
from objects.spaceship import Enemy
from objects.jank import Jank
from objects.world import World
from objects.world import Screen
import pygame
import random

# BUGS
# En la segunda o tercera BOX el enemy no muere
# A veces aparece el enemigo en la coordenada 0, 0
# Estoy mostrando las balas SOLO SI el enemigo esta vivo; cuando muere, no aparecen

pygame.font.init()
pygame.display.set_caption('Spaceship Virus')

world = World(
    width = 1300,
    height = 400,
    background_image = 'interface/images/space_background.png'
)

spaceship_screen = Screen(
    typing_text='Hola como estas',
    red_text='',
    green_text=''
)

player = Spaceship(
    speed = world.box,
    height = world.box,
    position = {
        'x_position': 0,
        'y_position': world.box*5
        }
)

enemy = [Enemy(
    speed = world.box,
    height = world.box,
    position = {
        'x_position': 1240,
        'y_position': random.randint(2, 11) * world.box
    }
    )]

game_screen = world.get_game_screen()
clock = pygame.time.Clock()
previous_bullet_position = {}

def draw(spaceship_bullets, user_string):

    dialogue_screen = pygame.draw.rect(game_screen, (255, 255, 255), pygame.Rect(0, 0, world.width, world.box))
    game_screen.blit(world.get_background(), (0, world.box*2))
    player.blit(game_screen)

    if not enemy == []:
        enemy[0].blit(game_screen)

    # Draw spaceship bullets
    for bullet in spaceship_bullets:
        if not enemy == []:
            if bullet.position == enemy[0].position:
                spaceship_bullets.remove(bullet)
                del enemy[0]
            else:
                bullet.blit(game_screen)
                previous_bullet_position[bullet] = bullet.position

    print(user_string)
    game_screen.blit(spaceship_screen.get_grey_text(), dialogue_screen)
    if user_string == spaceship_screen.typing_text[:len(user_string)]:
        game_screen.blit(spaceship_screen.get_green_text(user_string), dialogue_screen)
    


    pygame.display.update()


def main():

    running: bool = True
    spaceship_bullets: list = []
    user_string = ''
    

    while running:

        clock.tick(30)        

        # If player does something...
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if keys[pygame.K_UP]:
                player.move_up()
            if keys[pygame.K_DOWN]:
                player.move_down()

            # Si la letra que el usuario tecleo matchea con el string en la screen, entonces aparece en verde
            # Si la letra del usuario no matchea, entonces la letra aparece en rojo y no sobreescribe el user_string


            if event.type == pygame.KEYDOWN:
                user_string += event.unicode
            if keys[pygame.K_BACKSPACE]:
                user_string = user_string[:-1]
            #if event.type == pygame.K_SPACE:
                #user_string = ''

        if not spaceship_bullets == []:
            for bullet in spaceship_bullets:
                bullet.move_to_right(world.width, spaceship_bullets)
                if not enemy == []:
                    if enemy[0].position['x_position'] == round(bullet.position['x_position']) and enemy[0].position['y_position'] == round(bullet.position['y_position']):
                        enemy[0].life = 0

        # Draw player, spaceship_bullets and enemies
        draw(spaceship_bullets, user_string)

    pygame.quit()

if __name__ == "__main__":
    main()