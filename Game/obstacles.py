
import pygame.image
from numpy.random import randint

class Obstacles(object):

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        #
        # Base
        #
        self.base_image = pygame.image.load('imgs/base.png').convert_alpha()
        self.base_x = 0
        self.base_y = self.screen_height * 0.90
        self.base_shift = self.base_image.get_width() - self.screen_width
        #
        # Pipes
        #
        pipe_image = pygame.image.load('imgs/pipe.png')
        self.pipe_images = [pygame.transform.rotate(pipe_image.convert_alpha(), 180), pipe_image.convert_alpha()]
        self.pipe_hit_mask = [pygame.surfarray.pixels_alpha(image).astype(bool) for image in self.pipe_images]
        self.pipe_velocity_x = -4

        self.pipe_width = self.pipe_images[0].get_width()
        self.pipe_height = self.pipe_images[0].get_height()
        pipes = [self.generate_pipe(), self.generate_pipe()]

        pipes[0]["x_upper"] = pipes[0]["x_lower"] = self.screen_width
        pipes[1]["x_upper"] = pipes[1]["x_lower"] = self.screen_width * 1.5
        self.pipes = pipes

    def generate_pipe(self):
        x = self.screen_width + 10
        max_visible_pipe_on_screen = self.screen_height - self.pipe_height

        y_upper_with_gap = 0
        y_lower_with_gap = max_visible_pipe_on_screen

        rnd_gap_between_pipes = randint(self.screen_height * 0.20, self.screen_height * 0.30)
        gap_between_pipes = 120
        y_upper_with_gap -= gap_between_pipes
        y_lower_with_gap += gap_between_pipes

        max_rnd_y = (self.screen_height * 0.15)
        rnd_y = randint(-max_rnd_y, max_rnd_y)
        y_upper_with_gap -= rnd_y
        y_lower_with_gap -= rnd_y

        return {
            "x_upper": x,
            "y_upper": y_upper_with_gap,
            "x_lower": x,
            "y_lower": y_lower_with_gap
        }

    def update(self):
        # Update base position
        self.base_x = -((-self.base_x + 100) % self.base_shift)
        # Update pipes' position
        for pipe in self.pipes:
            pipe["x_upper"] += self.pipe_velocity_x
            pipe["x_lower"] += self.pipe_velocity_x
        # Update pipes
        if 0 < self.pipes[0]["x_lower"] < 5:
            self.pipes.append(self.generate_pipe())
        if self.pipes[0]["x_lower"] < -self.pipe_width:
            del self.pipes[0]

    def render(self):
        # Pipes
        for pipe in self.pipes:
            self.screen.blit(self.pipe_images[0], (pipe["x_upper"], pipe["y_upper"]))
            self.screen.blit(self.pipe_images[1], (pipe["x_lower"], pipe["y_lower"]))

        # Base
        self.screen.blit(self.base_image, (self.base_x, self.base_y))