import pygame

class World:
    def __init__(self, width, height, background_image):
        self.width = width
        self.height = height
        self.box = round(self.height / 13)
        self.background_image = background_image

    def get_background(self):
        return pygame.transform.scale(pygame.image.load(self.background_image), (self.width, self.box*10)).convert()
    
    def take_borders_out(self):
        return pygame.NOFRAME

    def get_game_screen(self):
        return pygame.display.set_mode((self.width, self.height), self.take_borders_out())
    
class Screen:
    def __init__(self, user_string, typing_text, red_text, green_text):
        self.user_string = user_string
        self.typing_text = typing_text
        self.red_text = red_text
        self.green_text = green_text

    def get_user_input(self):
        return input()
    
    def get_screen_font(self):
        return pygame.font.Font(None, 32)
    
    def get_grey_text(self):
        return self.get_screen_font().render(self.typing_text, True, (175, 175, 175))
    
    def get_green_text(self, user_string):
        return self.get_screen_font().render(user_string, True, (58, 188, 35))
    