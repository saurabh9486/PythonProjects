import pygame
from pygame.locals import *
import time
import random
SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/apple.jpg").convert()
        self.block_x = SIZE*3
        self.block_y = SIZE*3

    def draw_apple(self):
        self.parent_screen.blit(self.block, (self.block_x, self.block_y))
        pygame.display.flip()

    def move(self):
        self.block_x = random.randint(0, 24) * SIZE
        self.block_y = random.randint(0, 19) * SIZE
        # self.draw_apple()


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block_x = [SIZE] * length
        self.block_y = [SIZE] * length
        self.direction = 'down'

    def draw_block(self):
        self.parent_screen.fill((200, 220, 0))

        # Draw the image to the screen at the given position.
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))

        # display.flip() will update the contents of the entire display.
        # display.update() allows to update a portion of the screen,
        # instead of the entire area of the screen.
        # Passing no arguments, updates the entire display.
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def set_direction(self):

        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == 'up':
            self.block_y[0] -= SIZE
            self.draw_block()

        if self.direction == 'down':
            self.block_y[0] += SIZE
            self.draw_block()

        if self.direction == 'left':
            self.block_x[0] -= SIZE
            self.draw_block()

        if self.direction == 'right':
            self.block_x[0] += SIZE
            self.draw_block()

    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((200, 220, 0))

        self.snake = Snake(self.surface, 1)
        self.snake.draw_block()

        self.apple = Apple(self.surface)
        self.apple.draw_apple()

    def play(self):
        self.snake.set_direction()
        self.apple.draw_apple()
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.block_x, self.apple.block_y):
            self.snake.increase_length()
            self.apple.move()
        self.display_score()
        pygame.display.flip()

    def is_collision(self, x_s, y_s, x_a, y_a):
        if (x_s >= x_a) and (x_s < (x_a + SIZE)):
            if (y_s >= y_a) and (y_s < (y_a + SIZE)):
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 40, italic=True)
        score = font.render(f"Score : {self.snake.length - 1}", True, (255,255,255))
        self.surface.blit(score, (800, 20))

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.3)

        pass


if __name__ == '__main__':
    game = Game()
    game.run()
