from objects.spaceship import Spaceship, Enemy
from objects.world import World, Screen
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

world = World(
    width = 1300,
    height = 400,
    background_image_source = 'interface/images/space_background.png'
)

aupper_screen = Screen(
    user_string= '',
    typing_text='',
    red_text='',
    green_text=''
)

alower_screen = Screen(
    user_string= '',
    typing_text='',
    red_text='',
    green_text=''
)

player = Spaceship(
    x_position = 0,
    y_position = world.box*5,
    box = world.box
)

enemy = Enemy(
    x_position = world.width-50,
    y_position = random.randint(2, 10)*world.box,
    box = world.box
    )

spaceship_bullets = pygame.sprite.Group()

game_screen = pygame.display.set_mode((world.width, world.height), pygame.NOFRAME)
clock = pygame.time.Clock()
previous_bullet_position = {}

def draw(spaceship_bullets):

    # DIALOGUE SCREEN
    dialogue_screen = pygame.Surface((world.width, world.box))
    dialogue_screen_rect = dialogue_screen.get_rect(topleft = (0, 0))

    # UPPER SCREEN
    upper_screen = pygame.Surface((world.width, world.box))
    upper_screen_rect = upper_screen.get_rect(topleft = (dialogue_screen_rect.bottomleft))

    # PLAYING RECTANGLE
    gaming_screen = pygame.Surface((world.width, world.box*10))
    gaming_screen_rect = gaming_screen.get_rect(topleft = (upper_screen_rect.bottomleft))
    background = pygame.image.load(world.background_image_source).convert_alpha()
    game_screen.blit(background, gaming_screen_rect)

    spaceship = pygame.image.load(player.spaceship_source).convert_alpha()
    spaceship_rect = spaceship.get_rect(topleft = (player.x_position, player.y_position))
    game_screen.blit(spaceship, spaceship_rect)

    enemy_spaceship = pygame.image.load(enemy.spaceship_source).convert_alpha()
    enemy_rect = enemy_spaceship.get_rect(topleft = (enemy.x_position, enemy.y_position))
    game_screen.blit(enemy_spaceship, enemy_rect)

    # LOWER SCREEN
    lower_screen = pygame.Surface((world.width, world.height-world.box))
    lower_screen_rect = lower_screen.get_rect(bottomleft = (0, world.height))
    game_screen.blit(lower_screen, lower_screen_rect)


    pygame.display.update()

'''    # Draw spaceship bullets
    for bullet in spaceship_bullets:
        if not enemy == []:
            if bullet.position == enemy[0].position:
                spaceship_bullets.remove(bullet)
                del enemy[0]
            else:
                bullet.blit(game_screen)
                previous_bullet_position[bullet] = bullet.position

    game_screen.blit(upper_screen.get_grey_text(), upper_screen_rect)
    game_screen.blit(lower_screen.get_grey_text(), lower_screen_rect)

    if refresh_user_and_typing_text_us:
        upper_screen.typing_text = ''
        upper_screen.user_string = ''
    if refresh_user_and_typing_text_ls:
        lower_screen.typing_text = ''
        lower_screen.user_string = ''
    if blit_user_text_us:
        game_screen.blit(upper_screen.get_green_text(), upper_word_screen)
    if blit_user_text_ls:
        game_screen.blit(lower_screen.get_green_text(), lower_word_screen)'''

    


def main():
    # Block ALL events from being on the queue
    pygame.event.set_blocked(None)
    # Allow just this event to be on the queue
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

    running = True

    while running:
        # Setting FPS
        clock.tick(60)

#        refresh_user_and_typing_text_us: bool = False
#        blit_user_text_us: bool = False
#        refresh_user_and_typing_text_ls: bool = False
#        blit_user_text_ls: bool = False
#
#        if upper_screen.typing_text == '':
#            upper_screen.typing_text = r.get_random_word()
#        if lower_screen.typing_text == '':
#            lower_screen.typing_text = r.get_random_word()

        # If player does something...
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
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
                player.move_up()

            if keys[pygame.K_DOWN]:
                player.move_down()

#            if keys[pygame.K_BACKSPACE]:
#                upper_screen.user_string = upper_screen.user_string[:-1]
#                lower_screen.user_string = lower_screen.user_string[:-1]
#                continue

#            if event.type == pygame.KEYDOWN:
#                upper_screen.update_word_if_match_next_letter(event.unicode)
#                lower_screen.update_word_if_match_next_letter(event.unicode)

        if not spaceship_bullets == []:
            for bullet in spaceship_bullets:
                bullet.update()
                if not enemy == []:
                    if enemy[0].position['x_position'] == round(bullet.position['x_position']) and enemy[0].position['y_position'] == round(bullet.position['y_position']):
                        enemy[0].life = 0


#        if upper_screen.user_string == upper_screen.typing_text:
#            refresh_user_and_typing_text_us = True
#            player.move_up()
#        elif upper_screen.match_until_now():
#            blit_user_text_us = True
#        else:
#            blit_user_text_us = True

#        if lower_screen.user_string == lower_screen.typing_text:
#            refresh_user_and_typing_text_ls = True
#            player.move_down()
#        elif lower_screen.match_until_now():
#            blit_user_text_ls = True
#        else:
#            blit_user_text_ls = True

        # Draw player, spaceship_bullets and enemies
        draw(spaceship_bullets)

    pygame.quit()

if __name__ == "__main__":
    main()