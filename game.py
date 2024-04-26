from objects.spaceship import Spaceship
from objects.jank import Jank
import pygame
import random
import time

#pygame.display.set_caption('Spaceship Virus')
WIDTH = 1300
HEIGHT = 400
# Remember to divide Y position and subtract half of the spaceship height
player = Spaceship(speed=HEIGHT/10, height=HEIGHT/10, enemy=False, position={'x_position': 0, 'y_position': (HEIGHT/10)*5})
enemy = Spaceship(speed=HEIGHT/10, height=HEIGHT/10, enemy=True, position={'x_position': 1200, 'y_position': random.randint(0, 400)})
# This flag takes borders out
flags = pygame.NOFRAME
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
background = pygame.transform.scale(pygame.image.load('interface/images/space_pixel_art.png'), (WIDTH, HEIGHT)).convert()

clock = pygame.time.Clock()


def draw(player_spaceship, bullets, enemies):

    # Draw background and player
    screen.blit(background, (0, 0))
    screen.blit(player_spaceship, (player.position['x_position'], player.position['y_position']))

    # Draw enemies
    if not enemies == []:
        for e in enemies:
            screen.blit(e['itself'], (e['x'], e['y']))

    # Draw enemy's bullets
    if not bullets == []:
        bullets_copy = bullets.copy()
        for bullet in bullets_copy:
            if bullet['enemy'] == False:
                bullet['x'] += 1
                screen.blit(bullet['itself'], (bullet['x'], bullet['y']))
            elif bullet['enemy'] == True:
                bullet['x'] -= 1
                screen.blit(bullet['itself'], (bullet['x'], bullet['y']))
            
    pygame.display.update()


def main():
    running: bool = True

    start_time = time.time()
    elapsed_time = 0

    bullets: list = []
    enemies: list = []

    while running:

        clock.tick(60)
        elapsed_time = time.time() - start_time

        # Enemy render and enemy bullet render
        if elapsed_time >= 2:
            if len(enemies) < 3:
                enemies.append({'itself': enemy, 'x': enemy.position['y_position'], 'y': enemy.position['x_position']})

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
                player.shoot()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()

        # Draw player, bullets and enemies
        draw(player.scaled_spaceship_image(), bullets, enemies)

    pygame.quit()

if __name__ == "__main__":
    main()