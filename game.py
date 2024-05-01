from objects.spaceship import Spaceship
from objects.spaceship import Enemy
from objects.jank import Jank
import pygame
import random

# BUGS
# En la segunda o tercera BOX el enemy no muere
# A veces aparece el enemigo en la coordenada 0, 0

pygame.display.set_caption('Spaceship Virus')
WIDTH = 1300
HEIGHT = 700
BOX = round(HEIGHT / 13)
# Remember to divide Y position and subtract half of the spaceship height
player = Spaceship(speed=BOX, height=BOX, position={'x_position': 0, 'y_position': BOX*5})
enemy = [Enemy(speed=BOX, height=BOX, position={'x_position': 1200, 'y_position': random.randint(2, 11) * BOX})]
# This flag takes borders out
flags = pygame.NOFRAME
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
background = pygame.transform.scale(pygame.image.load('interface/images/space_background.png'), (WIDTH, BOX*10)).convert()
clock = pygame.time.Clock()
previous_bullet_position = {}


def draw(spaceship_bullets):

    # Draw background, player and enemy
    screen.blit(background, (0, BOX*2))
    player.blit(screen)
    # Solo lo estoy dejando de mostrar
    if not enemy == []:
        enemy[0].blit(screen)

    # Draw spaceship bullets
    if not spaceship_bullets == []:
        for bullet in spaceship_bullets:
            if not enemy == []:
                if bullet.position == enemy[0].position:
                    del bullet
                    del enemy[0]
                else:
                    bullet.blit(screen)
                    previous_bullet_position[bullet] = bullet.position
            
    pygame.display.update()


def main():
    running: bool = True
    spaceship_bullets: list = []
    enemy_moved: bool = False

    while running:

        clock.tick(60)        

        # If player does something...
        for event in pygame.event.get():

            # If press quit then Quit
            if event.type == pygame.QUIT:
                running = False
                break

            # If press keys...
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player.move_up()
            if keys[pygame.K_DOWN]:
                player.move_down()
            if keys[pygame.K_SPACE]:
                beam = (
                    Jank(height=BOX, speed=40, position={
                        'x_position': player.position['x_position'] + player.position['x_position'] / 2,
                        'y_position': player.position['y_position']
                    })
                )
                spaceship_bullets.append(beam)

            if keys[pygame.K_w] and not enemy_moved:
                enemy[0].move_up()
                enemy_moved = True
            elif keys[pygame.K_w]:
                enemy_moved = False

            if keys[pygame.K_s] and not enemy_moved:
                enemy[0].move_down()
                enemy_moved = True
            elif keys[pygame.K_s]:
                enemy_moved = False


            if keys[pygame.K_ESCAPE]:
                pygame.quit()

        if not spaceship_bullets == []:
            for bullet in spaceship_bullets:
                bullet.move_to_right(WIDTH, spaceship_bullets)
                if not enemy == []:
                    if enemy[0].position['x_position'] == round(bullet.position['x_position']) and enemy[0].position['y_position'] == round(bullet.position['y_position']):
                        enemy[0].life = 0

        # Draw player, spaceship_bullets and enemies
        draw(spaceship_bullets)

    pygame.quit()

if __name__ == "__main__":
    main()