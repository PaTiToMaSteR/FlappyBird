import pygame
import numpy as np

from Game.background import Background
from Game.bird import Bird
from Game.obstacles import Obstacles

screen_width = 288
screen_height = 512
fps = 30

class BirdPerformance(object):

    def __init__(self):
        self.score = 0
        self.reward = 0


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption('PyTorch Flappy Bird')
    # sets the window size
    screen = pygame.display.set_mode((screen_width, screen_height))

    bg = Background(screen)
    bird = Bird(screen, screen_width, screen_height)
    bird_performance = BirdPerformance()
    obstacles = Obstacles(screen, screen_width, screen_height)
    fps_clock = pygame.time.Clock()

    # infinite loop
    while True:
        # gets a single event from the event queue
        events = pygame.event.get()
        #
        # Flap or not
        #
        action = 0

        for event in events:
            if event is not None:
                # if the 'close' button of the window is pressed
                if event.type == pygame.QUIT:
                    # finalizes Pygame
                    pygame.quit()
                    break

                # captures the 'KEYDOWN' and 'KEYUP' events
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    # gets the key name
                    key_name = pygame.key.name(event.key)

                    # converts to uppercase the key name
                    key_name = key_name.upper()

                    # if any key is pressed
                    if event.type == pygame.KEYDOWN and key_name == "UP":
                        action = 1

                    #elif event.type == pygame.KEYUP:
                    #    print('"{}" key released'.format(key_name))
        #
        # Update
        #
        bird.update(action)
        obstacles.update()
        #
        # Update score
        #
        bird_center_x = bird.bird_x + bird.bird_width / 2
        for pipe in obstacles.pipes:
            pipe_center_x = pipe["x_upper"] + obstacles.pipe_width / 2
            if pipe_center_x < bird_center_x < pipe_center_x + 5:
                bird_performance.score += 1
                bird_performance.reward = 1
                break

        def has_bird_collided_with_pipes(bird, obstacles):
            # Check if the bird touch ground
            if bird.bird_height + bird.bird_y + 1 >= obstacles.base_y:
                return True
            bird_bbox = pygame.Rect(bird.bird_x, bird.bird_y, bird.bird_width, bird.bird_height)
            pipe_boxes = []
            for pipe in obstacles.pipes:
                pipe_boxes.append(pygame.Rect(pipe["x_upper"], pipe["y_upper"], obstacles.pipe_width, obstacles.pipe_height))
                pipe_boxes.append(pygame.Rect(pipe["x_lower"], pipe["y_lower"], obstacles.pipe_width, obstacles.pipe_height))
                # Check if the bird's bounding box overlaps to the bounding box of any pipe
                if bird_bbox.collidelist(pipe_boxes) == -1:
                    return False
                for i in range(2):
                    cropped_bbox = bird_bbox.clip(pipe_boxes[i])
                    min_x1 = cropped_bbox.x - bird_bbox.x
                    min_y1 = cropped_bbox.y - bird_bbox.y
                    min_x2 = cropped_bbox.x - pipe_boxes[i].x
                    min_y2 = cropped_bbox.y - pipe_boxes[i].y
                    if np.any(bird.bird_hitmask[bird.bird_index][min_x1:min_x1 + cropped_bbox.width,
                              min_y1:min_y1 + cropped_bbox.height] * obstacles.pipe_hit_mask[i][
                                                                     min_x2:min_x2 + cropped_bbox.width,
                                                                     min_y2:min_y2 + cropped_bbox.height]):
                        return True
            return False

        if has_bird_collided_with_pipes(bird, obstacles):
            bird_performance.reward = -1
            main()  # restart the game

        #
        # Render
        #
        bg.render()
        bird.render()
        obstacles.render()

        #from src.utils import pre_processing
        #image = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()

        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
