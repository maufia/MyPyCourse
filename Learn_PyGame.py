"""Learn PyGame package with few examples"""

import os
import sys
import random
import click
import pygame


def random_direction(speed: int) -> list:
    """Generates a random direction and speed for the moving object
    :param speed: speed on the x and y axis
    :return: a tuple with speeds which can be positive or negative
    """
    directions = [-1, 1, 0]
    x_direction = random.choice(directions)
    y_direction = random.choice(directions)
    while 42:
        if random.uniform(0, 1) > 0.95:
            x_direction = random.choice(directions)
            y_direction = random.choice(directions)
        yield speed * x_direction, speed * y_direction


class MovingObject:
    """Class for moving objects"""

    def __init__(self, size_field: list, speed: int):
        """
        Create a moving object
        :param size_field:
        :param speed:
        """
        self.size_field = size_field
        self.speed = speed
        self.dot, self.dot_rect = self.make_moving_item()
        self.get_direction = random_direction(self.speed)

    def make_moving_item(self) -> tuple:
        """
        Make a moving item
        Random initialise position
        :return:  True
        """
        dot = pygame.image.load(os.path.join('Images'dd.png'))
        dot_rect = dot.get_rect()
        dot_rect = dot_rect.move(random.randint(0, self.size_field[0]),
                                 random.randint(0, self.size_field[1]))
        return dot, dot_rect

    def get_next_location(self) -> pygame.Rect:
        """Get next location from speed
        :return:
        """
        p = next(self.get_direction)
        dot_rect = self.dot_rect.move(p[0], p[1])
        self.dot_rect = self._check_edges(dot_rect)
        return self.dot_rect

    def _check_edges(self, dot_rect: pygame.Rect) -> pygame.Rect:
        """ Ensure that the dot is within the window
        If itgoes out one side,it returns from other
        :param dot_rect: the position of the dot
        :return: the corrected position of the dot
        """
        if dot_rect[0] < 0:
            dot_rect[0] = self.size_field[0] - 1
        if dot_rect[1] < 0:
            dot_rect[1] = self.size_field[1] - 1
        if dot_rect[0] >= self.size_field[0]:
            dot_rect[0] = 0
        if dot_rect[1] >= self.size_field[1]:
            dot_rect[1] = 0
        # print(dot_rect)
        return dot_rect


def start_game(n_moving_dots: int, size_field: list) -> True:
    """ Set up pygame

    :param n_moving_dots: number of moving dots
    :param size_field: size of the field
    :return: True
    """
    pygame.init()
    speeds = range(1, 4)
    black = [0, 0, 0]
    screen = pygame.display.set_mode(size_field)
    # Create n moving dots, all randomly positioned in the field
    dots = [MovingObject(size_field, random.choice(speeds)) for _ in
            range(n_moving_dots)]
    game_clock = pygame.time.Clock()

    while 42:
        game_clock.tick(50)  # framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        [screen.blit(d.dot, d.get_next_location()) for d in dots]
        pygame.display.flip()


def get_arguments() -> True:
    """
    Get arguments from command line
    :return: True
    """

    @click.group(help='CLI for Learn_Pygame')
    @click.option('--n_moving_items', '-n', default=100,
                  type=click.IntRange(1, 1e4),
                  help='Number of moving items. Default: 100, Range: [1,1e4]')
    @click.option('--size_field', '-sz', nargs=2, default=(500, 500),
                  type=click.Tuple([click.IntRange(1, 5000),
                                    click.IntRange(1, 5000)]),
                  help='X, Y size of the field. ' +
                       'Default: [50,50], Range: [1...5000]')
    @click.pass_context
    def cli(ctx, n_moving_items, size_field):
        """CLI for Learn_Pygame"""
        ctx.obj['n_moving_items'] = n_moving_items
        ctx.obj['size_field'] = size_field

    @cli.command()
    @click.pass_context
    def run_game(ctx):
        """Start the game"""
        start_game(ctx.obj['n_moving_items'], ctx.obj['size_field'])

    cli(obj={})
    return True


# --------------------------------------------------


if __name__ == "__main__":
    get_arguments()
