import pygame
from pygame.locals import *

import sys


CHAR_WIDTH = 5
CHAR_HEIGHT = 10
CHAR_TOP_MARG = 2
CHAR_BOTTOM_MARG = 1

font_img = pygame.image.load("pixel_font.png")
print("a is ", ord("a"))
print("b is ", ord("b"))

def draw_text(text, surface):
    text_len = len(text)
    total_width = text_len * CHAR_WIDTH
    text_surface = pygame.Surface((total_width, CHAR_HEIGHT))
    for i, char in enumerate(text):
        surface.blit(font_img, (i * (CHAR_WIDTH+1), 0), ((ord(char)-97) * (CHAR_WIDTH+1), 0, CHAR_WIDTH, CHAR_HEIGHT))


class App:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((320, 200))

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.fill("white")
            draw_text("hellothere", self.display_surface)
            pygame.display.update()


App().run()
