from objects.spaceship import Spaceship
from objects.spaceship import Enemy
from objects.jank import Jank
import pygame
import random

pygame.display.set_caption('Spaceship Virus')
WIDTH = 1300
HEIGHT = 400
# Remember to divide Y position and subtract half of the spaceship height
player = Spaceship(speed=HEIGHT/10, height=HEIGHT/10, position={'x_position': 0, 'y_position': (HEIGHT/10)*5})
enemy = Enemy(speed=HEIGHT/10, height=HEIGHT/10, position={'x_position': 1220, 'y_position': random.randint(0, 10) * HEIGHT/10})
# This flag takes borders out
flags = pygame.NOFRAME
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
background = pygame.transform.scale(pygame.image.load('interface/images/space_background.png'), (WIDTH, HEIGHT)).convert()
clock = pygame.time.Clock()
previous_bullet_position = {}


def draw(bullets):

    # Draw background and player
    screen.blit(background, (0, 0))
    player.blit(screen)
    enemy.blit(screen)

    # Draw enemy's bullets
    if not bullets == []:
        for bullet in bullets:
            previous_position = previous_bullet_position.get(bullet)
            bullet.blit(screen)
            previous_bullet_position[bullet] = bullet.position
            
    pygame.display.update()


def main():
    running: bool = True
    bullets: list = []
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
                    Jank(height=HEIGHT/10, speed=50, position={
                        'x_position': player.position['x_position'] + player.position['x_position'] / 2,
                        'y_position': player.position['y_position']
                    })
                )
                bullets.append(beam)

            if keys[pygame.K_w] and not enemy_moved:
                enemy.move_up()
                enemy_moved = True
            elif keys[pygame.K_w]:
                enemy_moved = False

            if keys[pygame.K_s] and not enemy_moved:
                enemy.move_down()
                enemy_moved = True
            elif keys[pygame.K_s]:
                enemy_moved = False


            if keys[pygame.K_ESCAPE]:
                pygame.quit()

        for bullet in bullets:
            bullet.update(WIDTH, bullets)

        # Draw player, bullets and enemies
        draw(bullets)

    pygame.quit()

if __name__ == "__main__":
    main()