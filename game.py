from objects.spaceship import Spaceship
from objects.jank import Jank
import pygame

pygame.display.set_caption('Spaceship Virus')
player = Spaceship(speed=10)
screen = pygame.display.set_mode((1300, 400))
background = pygame.transform.scale(pygame.image.load('interface/images/space_pixel_art.png'), (1300, 400)).convert()

clock = pygame.time.Clock()


def draw(player_spaceship):
    screen.blit(background, (0, 0))
    screen.blit(player_spaceship, (player.position['x_position'], player.position['y_position']))

    pygame.display.update()


def main():

    running: bool = True
    clock.tick(60)
    player_spaceship = pygame.transform.scale(pygame.image.load(player.get_path()), (100, 150)).convert()
    bullet = pygame.transform.scale(pygame.image.load('interface/images/laser_beam2.png'), (20, 30)).convert()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player.move_up()
            if keys[pygame.K_DOWN]:
                player.move_down()

        draw(player_spaceship)


if __name__ == "__main__":
    main()