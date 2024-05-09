import pygame

class World:
    def __init__(self, width, height, background_image_source):
        self.width = width
        self.height = height
        self.box = round(self.height / 13)
        self.background_image_source = background_image_source
    
class Screen(World):
    def __init__(self, user_string, typing_text, red_text, green_text):
        self.user_string = user_string
        self.typing_text = typing_text
        self.red_text = red_text
        self.green_text = green_text
    
    def get_screen_font(self):
        return pygame.font.Font(None, 32)
    
    def get_grey_text(self):
        return self.get_screen_font().render(self.typing_text, True, (175, 175, 175))
    
    def get_green_text(self):
        return self.get_screen_font().render(self.user_string, True, (58, 188, 35))
    
    def update_word_if_match_next_letter(self, letter_pressed):
        if letter_pressed in self.typing_text:
            if self.typing_text[len(self.user_string):].startswith(letter_pressed):
                self.user_string += letter_pressed

    def match_until_now(self):
        return self.user_string == self.typing_text[:len(self.user_string)]