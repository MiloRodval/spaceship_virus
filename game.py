from objects.spaceship import Spaceship
from objects.bullet import Player_bullet, Enemy_bullet
from objects.enemy import Enemy
from random_word import RandomWords
import pygame, random

# BUGS
# A veces se escribe dos veces la misma letra

pygame.init()
pygame.font.init()
pygame.display.set_caption('Spaceship Virus')
r = RandomWords()
font = pygame.font.Font('./interface/fonts/retganon.ttf', 30)

WIDTH = 1500
HEIGHT = 750
BOX = round(HEIGHT / 13)

screen = 'interface/images/space_background.png'
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.sprite.GroupSingle()
player.add(Spaceship((10, BOX*3), BOX))

enemies = pygame.sprite.Group()
spaceship_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

clock = pygame.time.Clock()

def main():
    # Timer
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 5000)
    enemy_shooting_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_shooting_timer, 3000)

    update_upper_word = True
    update_lower_word = True
    update_shooting_word = True
    typed_upper = False
    typed_lower = False
    typed_shooting = False
    current_word = ''

    upper_random_word = r.get_random_word()
    update_upper_word = False

    while True:
        new_word = r.get_random_word()
        if new_word[0] != upper_random_word[0]:
            lower_random_word = new_word
            update_lower_word = False
            break

    while True:
        new_word = r.get_random_word()
        if new_word[0] != upper_random_word[0] and new_word[0] != lower_random_word[0]:
            shooting_random_word = new_word
            update_shooting_word = False
            break


    running = True
    while running:
        # Setting FPS
        clock.tick(60)

        # Update random words if condition is met
        while update_upper_word:
            new_word = r.get_random_word()
            if new_word[0] != lower_random_word[0] and new_word[0] != shooting_random_word[0]:
                upper_random_word = new_word
                update_upper_word = False

        while update_lower_word:
            new_word = r.get_random_word()
            if new_word[0] != upper_random_word[0] and new_word[0] != shooting_random_word[0]:
                lower_random_word = r.get_random_word()
                update_lower_word = False

        while update_shooting_word:
            new_word = r.get_random_word()
            if new_word[0] != lower_random_word[0] and new_word[0] != lower_random_word[0]:
                shooting_random_word = r.get_random_word()
                update_shooting_word = False 

        # If player does something...
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(current_word[:-1]) == 0:
                        typed_upper = False
                        typed_lower = False
                        typed_shooting = False
                    current_word = current_word[:-1]

            if event.type == pygame.TEXTINPUT:

                if event.text == upper_random_word[0]:
                    typed_upper = True
                if event.text == lower_random_word[0]:
                    typed_lower = True
                if event.text == shooting_random_word[0]:
                    typed_shooting = True
                

                if typed_upper:
                    if len(upper_random_word) > len(current_word) and event.text == upper_random_word[len(current_word)]:
                        current_word += event.text

                    if current_word == upper_random_word:
                        player.sprite.rect.move_ip(0, -player.sprite.speed)
                        update_upper_word = True
                        current_word = ''
                        typed_upper = False


                if typed_lower:
                    if len(lower_random_word) > len(current_word) and event.text == lower_random_word[len(current_word)]:
                        current_word += event.text

                    if current_word == lower_random_word:
                        player.sprite.rect.move_ip(0, player.sprite.speed)
                        update_lower_word = True
                        current_word = ''
                        typed_lower = False

                if typed_shooting:
                    if len(shooting_random_word) > len(current_word) and event.text == shooting_random_word[len(current_word)]:
                        current_word += event.text

                    if current_word == shooting_random_word:
                        spaceship_bullets.add(Player_bullet(WIDTH, 40, player.sprite.rect.midright))
                        update_shooting_word = True
                        current_word = ''
                        typed_lower = False

            if event.type == enemy_timer and len(enemies) <= 3:
                random_place = random.randint(2, 11) * BOX
                enemies.add(Enemy((WIDTH - 100, random_place), BOX, BOX*10))
            
            if event.type == enemy_shooting_timer:
                for enemy in enemies:
                    enemy_bullets.add(Enemy_bullet(10, enemy.rect.midleft))

        # DIALOGUE SCREEN
        dialogue_screen = pygame.Surface((WIDTH, BOX))
        dialogue_screen.fill((13, 2, 8))
        dialogue_screen_rect = dialogue_screen.get_rect(topleft = (0, 0))

        dialogue = font.render(f'{current_word = }', False, (0, 149, 17))
        dialogue_rect = dialogue.get_rect(midleft = (dialogue_screen_rect.midleft))

        game_screen.blit(dialogue_screen, dialogue_screen_rect)
        game_screen.blit(dialogue, dialogue_rect)

        # UPPER SCREEN
        upper_screen = pygame.Surface((WIDTH, BOX))
        upper_screen.fill((13, 0, 26))
        upper_screen_rect = upper_screen.get_rect(topleft = (dialogue_screen_rect.bottomleft))

        upper_word = font.render(upper_random_word, False, (0, 59, 0))
        current_word_font_upper = font.render(current_word, False, (0, 149, 17))
        upper_word_rect = upper_word.get_rect(midleft = (upper_screen_rect.midleft))

        game_screen.blit(upper_screen, upper_screen_rect)
        game_screen.blit(upper_word, upper_word_rect.midleft)
        if current_word == upper_random_word[:len(current_word)]:
            game_screen.blit(current_word_font_upper, upper_word_rect.midleft)


        # PLAYING SCREEN
        gaming_screen = pygame.Surface((WIDTH, BOX*10))
        gaming_screen_rect = gaming_screen.get_rect(topleft = (upper_screen_rect.bottomleft))
        background = pygame.image.load(screen).convert_alpha()

        game_screen.blit(background, gaming_screen_rect)

        # game_screen.blit(player.image, player.rect)
        player.draw(game_screen)

        spaceship_bullets.update()
        spaceship_bullets.draw(game_screen)

        enemy_bullets.update()
        enemy_bullets.draw(game_screen)

        for bullet in spaceship_bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy):
                    enemy.kill()
                    enemies_killed += 1

        for bullet in enemy_bullets:
            if bullet.rect.colliderect(player.sprite.rect):
                player.sprite.kill()
                break

        enemies.draw(game_screen)

        # LOWER SCREEN
        lower_screen = pygame.Surface((WIDTH, BOX))
        lower_screen.fill((13, 0, 26))

        #LEFT LOWER SCREEN
        left_lower_screen_rect = lower_screen.get_rect(topleft = gaming_screen_rect.bottomleft)
        lower_word = font.render(lower_random_word, False, (0, 59, 0))
        lower_word_rect = lower_word.get_rect(topleft = (gaming_screen_rect.bottomleft))
        current_word_font_lower = font.render(current_word, False, (0, 149, 17))

        game_screen.blit(lower_screen, left_lower_screen_rect)
        game_screen.blit(lower_word, lower_word_rect.midleft)
        if current_word == lower_random_word[:len(current_word)]:
            game_screen.blit(current_word_font_lower, lower_word_rect.midleft)

        # RIGHT LOWER SCREEN
        shooting_word = font.render(shooting_random_word, False, (0, 59, 0))
        shooting_word_rect = shooting_word.get_rect(midleft = (left_lower_screen_rect.center))
        current_word_font_shooting = font.render(current_word, False, (0, 149, 17))

        game_screen.blit(shooting_word, shooting_word_rect.topleft)
        if current_word == shooting_random_word[:len(current_word)]:
            game_screen.blit(current_word_font_shooting, shooting_word_rect.topleft)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
