
import pygame.image
from itertools import cycle


class Background(object):

    def __init__(self, screen):

        self.screen = screen
        self.background_image = pygame.image.load('imgs/bg.png').convert()
        self.background_image = pygame.image.load('imgs/bg.png').convert()

        self.bg_x_1 = 0
        self.bg_x_2 = self.background_image.get_width()

    def render(self):
        # Move both background images
        self.bg_x_1 -= 1.5
        self.bg_x_2 -= 1.5

        if self.bg_x_1 < self.background_image.get_width() * -1:  # If our bg is at the -width then reset its position
            self.bg_x_1 = self.background_image.get_width()

        if self.bg_x_2 < self.background_image.get_width() * -1:  # If our bg is at the -width then reset its position
            self.bg_x_2 = self.background_image.get_width()

        self.screen.blit(self.background_image, (self.bg_x_1, 0))
        self.screen.blit(self.background_image, (self.bg_x_2, 0))
