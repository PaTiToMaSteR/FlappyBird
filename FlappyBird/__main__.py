import pygame

from FlappyBird.background import Background
from FlappyBird.bird import Bird

screen_width = 288
screen_height = 512
fps = 30

def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption('PyTorch Flappy Bird')
    # sets the window size
    screen = pygame.display.set_mode((screen_width, screen_height))

    bg = Background(screen)
    bird = Bird(screen, screen_width, screen_height)
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
        #
        # Render
        #
        bg.render()
        bird.render()

        #from src.utils import pre_processing
        #image = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()

        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
