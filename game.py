from objects.world import World, Spaceship, Enemy, Screen
from objects.jank import Jank
from random_word import RandomWords
import pygame, random

# BUGS
# En la segunda o tercera BOX el enemy no muere
# A veces aparece el enemigo en la coordenada 0, 0
# Estoy mostrando las balas SOLO SI el enemigo esta vivo; cuando muere, no aparecen

pygame.init()
pygame.font.init()
pygame.display.set_caption('Spaceship Virus')
r = RandomWords()
font = pygame.font.Font('./interface/fonts/retganon.ttf', 30)

world = World(
    width = 1500,
    height = 750,
)

screen = Screen(
     background_image_source = 'interface/images/space_background.png',
)

player = Spaceship(
    x_position = 10,
    y_position = world.box*5,
    width = world.width,
    height = world.height,
)

enemy = Enemy(
    x_position = world.width-75,
    y_position = world.box*5,
    width = world.width,
    height = world.height,
    )

spaceship_bullets = pygame.sprite.Group()

game_screen = pygame.display.set_mode((world.width, world.height), pygame.NOFRAME)
clock = pygame.time.Clock()
previous_bullet_position = {}

def main():
    # Block ALL events from being on the queue
    pygame.event.set_blocked(None)
    # Allow just this event to be on the queue
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

    running = True
    upper_random_word = r.get_random_word()

    while running:
        # Setting FPS
        clock.tick(60)

        # If player does something...
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                pygame.quit()

            if keys[pygame.K_RIGHT]:
                    spaceship_bullets.add(
                        Jank(
                            height= world.box,
                            speed= 10,
                            position= player.position
                        )
                    )

            if keys[pygame.K_UP]:
                player.y_position -= player.speed

            if keys[pygame.K_DOWN]:
                player.y_position += player.speed

        # DIALOGUE SCREEN
        dialogue_screen = pygame.Surface((world.width, world.box))
        dialogue_screen.fill((13, 2, 8))
        dialogue_screen_rect = dialogue_screen.get_rect(topleft = (0, 0))

        dialogue = font.render(' - Seems like I\'m on space', None, (0, 149, 17))
        dialogue_rect = dialogue.get_rect(midleft = (dialogue_screen_rect.midleft))

        game_screen.blit(dialogue_screen, dialogue_screen_rect)
        game_screen.blit(dialogue, dialogue_rect)

        # UPPER SCREEN
        upper_screen = pygame.Surface((world.width, world.box))
        upper_screen.fill((13, 0, 26))
        upper_screen_rect = upper_screen.get_rect(topleft = (dialogue_screen_rect.bottomleft))

        upper_word = font.render(upper_random_word, None, (0, 149, 17))
        upper_word_rect = upper_word.get_rect(midleft = (upper_screen_rect.midleft))

        #ACA ESTOY
        game_screen.blit(upper_screen, upper_screen_rect)
        game_screen.blit(font.render(' * ', None, (0, 149, 17)), upper_word_rect.midleft)
        game_screen.blit(upper_word, upper_word_rect.midleft)

        # PLAYING RECTANGLE
        gaming_screen = pygame.Surface((world.width, world.box*10))
        gaming_screen_rect = gaming_screen.get_rect(topleft = (upper_screen_rect.bottomleft))
        background = pygame.image.load(screen.background_image_source).convert_alpha()

        game_screen.blit(background, gaming_screen_rect)

        spaceship = pygame.image.load(player.spaceship_source).convert_alpha()
        spaceship_scaled = pygame.transform.scale(spaceship, (75, world.box))
        spaceship_rect = spaceship_scaled.get_rect(topleft = (player.x_position, player.y_position))

        game_screen.blit(spaceship_scaled, spaceship_rect)

        enemy_spaceship = pygame.image.load(enemy.spaceship_source).convert_alpha()
        enemy_rect = enemy_spaceship.get_rect(topleft = (enemy.x_position, enemy.y_position))

        game_screen.blit(enemy_spaceship, enemy_rect)

        # LOWER SCREEN
        lower_screen = pygame.Surface((world.width, world.box))
        lower_screen.fill((13, 0, 26))
        lower_screen_rect = lower_screen.get_rect(bottomleft = (0, world.height))
        game_screen.blit(lower_screen, lower_screen_rect)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()