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
    background_image = 'interface/images/space_background.png'
)

upper_screen = Screen(
    user_string= '',
    typing_text='',
    red_text='',
    green_text=''
)

lower_screen = Screen(
    user_string= '',
    typing_text='',
    red_text='',
    green_text=''
)

player = Spaceship(
    speed = world.box,
    height = world.box,
    position = {
        'x_position': world.box,
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

spaceship_bullets = pygame.sprite.Group()

game_screen = world.get_game_screen()
clock = pygame.time.Clock()
previous_bullet_position = {}

def draw(spaceship_bullets, refresh_user_and_typing_text_us, blit_user_text_us, refresh_user_and_typing_text_ls, blit_user_text_ls):

    upper_word_screen = pygame.draw.rect(game_screen, (13, 0, 26), pygame.Rect(0, world.box, world.width, world.box*2))
    lower_word_screen = pygame.draw.rect(game_screen, (13, 0, 26), pygame.Rect(0, world.height - world.box, world.width, world.height))
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

    game_screen.blit(upper_screen.get_grey_text(), upper_word_screen)
    game_screen.blit(lower_screen.get_grey_text(), lower_word_screen)

    if refresh_user_and_typing_text_us:
        upper_screen.typing_text = ''
        upper_screen.user_string = ''
    if refresh_user_and_typing_text_ls:
        lower_screen.typing_text = ''
        lower_screen.user_string = ''
    if blit_user_text_us:
        game_screen.blit(upper_screen.get_green_text(), upper_word_screen)
    if blit_user_text_ls:
        game_screen.blit(lower_screen.get_green_text(), lower_word_screen)

    pygame.display.update()


def main():
    # Block ALL events from being on the queue
    pygame.event.set_blocked(None)
    # Allow just this event to be on the queue
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

    running: bool = True

    while running:
        # Setting FPS
        clock.tick(60)

        refresh_user_and_typing_text_us: bool = False
        blit_user_text_us: bool = False
        refresh_user_and_typing_text_ls: bool = False
        blit_user_text_ls: bool = False

        print(spaceship_bullets)

        if upper_screen.typing_text == '':
            upper_screen.typing_text = r.get_random_word()
        if lower_screen.typing_text == '':
            lower_screen.typing_text = r.get_random_word()

        # If player does something...
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if keys[pygame.K_UP]:
                    spaceship_bullets.add(
                        Jank(
                            height= world.box,
                            speed= 10,
                            position= player.position
                        )
                    )
            if keys[pygame.K_DOWN]:
                player.move_down()
            if keys[pygame.K_BACKSPACE]:
                upper_screen.user_string = upper_screen.user_string[:-1]
                lower_screen.user_string = lower_screen.user_string[:-1]
                continue

            if event.type == pygame.KEYDOWN:
                upper_screen.update_word_if_match_next_letter(event.unicode)
                lower_screen.update_word_if_match_next_letter(event.unicode)

        if not spaceship_bullets == []:
            for bullet in spaceship_bullets:
                bullet.update()
                if not enemy == []:
                    if enemy[0].position['x_position'] == round(bullet.position['x_position']) and enemy[0].position['y_position'] == round(bullet.position['y_position']):
                        enemy[0].life = 0


        if upper_screen.user_string == upper_screen.typing_text:
            refresh_user_and_typing_text_us = True
            player.move_up()
        elif upper_screen.match_until_now():
            blit_user_text_us = True
        else:
            blit_user_text_us = True

        if lower_screen.user_string == lower_screen.typing_text:
            refresh_user_and_typing_text_ls = True
            player.move_down()
        elif lower_screen.match_until_now():
            blit_user_text_ls = True
        else:
            blit_user_text_ls = True

        # Draw player, spaceship_bullets and enemies
        draw(spaceship_bullets, refresh_user_and_typing_text_us, blit_user_text_us, refresh_user_and_typing_text_ls, blit_user_text_ls)

    pygame.quit()

if __name__ == "__main__":
    main()