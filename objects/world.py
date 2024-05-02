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
    def __init__(self, text_on_screen):
        self.text_on_screen = text_on_screen

    def get_user_input(self):
        return input()
    
    def get_screen_font(self):
        return pygame.font.Font(None, 32)
    
    def get_screen_text(self):
        return self.get_screen_font().render(self.text_on_screen, True, (0, 255, 255))