from objects.spaceship import Spaceship
from objects.jank import Jank
import pygame
import random
import time

pygame.display.set_caption('Spaceship Virus')
player = Spaceship(speed=10)
enemy = Spaceship(speed=10)
screen = pygame.display.set_mode((1300, 400))
background = pygame.transform.scale(pygame.image.load('interface/images/space_pixel_art.png'), (1300, 400)).convert()

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

    bullet = Jank()
    bullets: list = []
    enemies: list = []

    while running:

        clock.tick(60)
        elapsed_time = time.time() - start_time

        # Enemy render and enemy bullet render
        if elapsed_time >= 2:
            if len(enemies) < 3:
                enemies.append({'itself': enemy.scaled_spaceship_image(), 'x': 1200, 'y': random.randint(-50, 300)})
            bullets.append({'itself': bullet.scaled_bullet_image(), 'x': 1200, 'y': random.randint(-50, 300), 'enemy': True})
            start_time = time.time()

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
                bullets.append({'bullet': bullet.scaled_bullet_image(), 'x': player.position['x_position'], 'y': player.position['y_position'], 'enemy': False})

        # Draw player, bullets and enemies
        draw(player.scaled_spaceship_image(), bullets, enemies)

    pygame.QUIT()

if __name__ == "__main__":
    main()