import pygame.image
from itertools import cycle
import numpy

class Bird(object):

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bird_images = [
            pygame.image.load('imgs/bird1.png').convert_alpha(),
            pygame.image.load('imgs/bird2.png').convert_alpha(),
            pygame.image.load('imgs/bird3.png').convert_alpha()
        ]

        self.bird_hitmask = [pygame.surfarray.pixels_alpha(image).astype(bool) for image in self.bird_images]
        self.bird_width = self.bird_images[0].get_width()
        self.bird_height = self.bird_images[0].get_height()

        self.bird_x = int(screen_width / 5)
        self.bird_y = int((screen_height - self.bird_height) / 2)

        # properties
        self.current_velocity_y = 0
        self.min_velocity_y = -8
        self.max_velocity_y = 10
        self.downward_speed = 1
        self.upward_speed = -9

        self.bird_index_generator = cycle([0, 1, 2, 1])
        self.bird_index = 0
        self.score = 0

    def update(self, action):  # 1 == flap, 0 == nothing

        # Check if we flapped
        if action == 1:
            self.current_velocity_y = self.upward_speed
        # Apply gravity
        elif self.current_velocity_y < self.max_velocity_y:
            self.current_velocity_y += self.downward_speed

        # Advance the sprite
        self.bird_index = next(self.bird_index_generator)

        # Set bird Y position and clamp just enough to be "self.bird_height" outside of the screen
        self.bird_y += self.current_velocity_y
        self.bird_y = numpy.clip(self.bird_y, -self.bird_height, self.screen_height)

    def get_y(self):
        return self.bird_y

    def render(self):

        # Draw everything
        self.screen.blit(self.bird_images[self.bird_index], (self.bird_x, self.bird_y))
