from objects.spaceship import Spaceship, Enemy
from objects.world import World, Screen
from random_word import RandomWords
import pygame, random

# BUGS
# En la segunda o tercera BOX el enemy no muere
# A veces aparece el enemigo en la coordenada 0, 0
# Estoy mostrando las balas SOLO SI el enemigo esta vivo; cuando muere, no aparecen

pygame.font.init()
pygame.display.set_caption('Spaceship Virus')
r = RandomWords()

world = World(
    width = 1300,
    height = 400,
    background_image = 'interface/images/space_background.png'
)

spaceship_screen = Screen(
    user_string= '',
    typing_text='',
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

def draw(spaceship_bullets, refresh_user_and_typing_text, blit_user_text):

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

    game_screen.blit(spaceship_screen.get_grey_text(), dialogue_screen)

    if refresh_user_and_typing_text:
        spaceship_screen.typing_text = ''
        spaceship_screen.user_string = ''
    if blit_user_text:
        game_screen.blit(spaceship_screen.get_green_text(spaceship_screen.user_string), dialogue_screen)

    pygame.display.update()


def main():

    running: bool = True
    spaceship_bullets: list = []
    matching = False

    while running:

        clock.tick(30)

        refresh_user_and_typing_text: bool = False
        blit_user_text: bool = False

        if spaceship_screen.typing_text == '':
            spaceship_screen.typing_text = r.get_random_word()   

        # If player does something...
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if keys[pygame.K_UP]:
                player.move_up()
            if keys[pygame.K_DOWN]:
                player.move_down()
            if keys[pygame.K_BACKSPACE]:
                spaceship_screen.user_string = spaceship_screen.user_string[:-1]
                continue

            if event.type == pygame.KEYDOWN:
                if event.unicode in spaceship_screen.typing_text:
                    if spaceship_screen.typing_text[len(spaceship_screen.user_string):].startswith(event.unicode):
                        spaceship_screen.user_string += event.unicode

        if not spaceship_bullets == []:
            for bullet in spaceship_bullets:
                bullet.move_to_right(world.width, spaceship_bullets)
                if not enemy == []:
                    if enemy[0].position['x_position'] == round(bullet.position['x_position']) and enemy[0].position['y_position'] == round(bullet.position['y_position']):
                        enemy[0].life = 0

        if spaceship_screen.user_string == spaceship_screen.typing_text:
            refresh_user_and_typing_text = True
        elif spaceship_screen.user_string == spaceship_screen.typing_text[:len(spaceship_screen.user_string)]:
            blit_user_text = True
        else:
            blit_user_text = True
            matching = False

        # Draw player, spaceship_bullets and enemies
        draw(spaceship_bullets, refresh_user_and_typing_text, blit_user_text)

    pygame.quit()

if __name__ == "__main__":
    main()

'''
Si matchean agrega la letra al string del usuario y mostralo
si no matchea no agregues la letra, pero mostra lo antetriormente escriot
'''