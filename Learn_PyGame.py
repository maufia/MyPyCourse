"""Learn PyGame package with few examples"""

import os
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


class MovingUEs:
    """Class for moving objects"""
    def __init__(self, size_field: list, speed: int):
        """
        Create a moving object
        :param size_field:
        :param speed:
        """
        self.size_field = size_field
        self.speed = speed
        self.figure, self.rect = self.make_moving_item()
        self.get_direction = random_direction(self.speed)

    def make_moving_item(self) -> tuple:
        """
        Make a moving item
        Random initialise position
        :return:  True
        """
        figure = pygame.image.load(os.path.join('Images', 'star_blue.png'))
        rect = figure.get_rect()
        rect = rect.move(random.randint(0, self.size_field[0]),
                         random.randint(0, self.size_field[1]))
        return figure, rect

    def get_next_location(self) -> pygame.Rect:
        """Get next location from speed
        :return:
        """
        p = next(self.get_direction)
        rect = self.rect.move(p[0], p[1])
        self.rect = self._check_edges(rect)
        return self.rect

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


class CityBackground:
    """ Create the fixed elements """
    def __init__(self, size_field):
        """
        These elements depend on the size of the map

        :param size_field: Size of the figure
        """
        self.surface = pygame.Surface(size_field).convert()
        self._objects = []
        self.add_city_map()
        self.add_antennas(size_field)
        self.generate_surface()

    def add_city_map(self) -> True:
        """Add the city map """
        figure_pos = (0, 0)
        city_map = pygame.image.load(os.path.join('Images',
                                                  'city.png')).convert()
        self._objects.append([city_map, figure_pos])
        return True

    def add_antennas(self, size_field) -> True:
        """ Add the antennas

        :param size_field: Size of the figure
        :return: True
        """
        #  for figure_pos in []
        return True

    def generate_surface(self) -> True:
        """

        :return: True
        """
        [self.surface.blit(fig, pos) for fig, pos in self._objects]
        return True


def start_game(n_moving_ues: int, size_field: list) -> True:
    """ Set up pygame

    :param n_moving_ues: number of moving user equipment
    :param size_field: size of the field
    :return: True
    """
    pygame.init()
    screen = pygame.display.set_mode(size_field)
    pygame.display.set_caption("Learn_PyGame")
    # Create n moving UEs, all randomly positioned in the field
    speeds = range(1, 4)
    user_equip = [MovingUEs(size_field, random.choice(speeds)) for _ in
                  range(n_moving_ues)]
    background = CityBackground(size_field)
    game_clock = pygame.time.Clock()

    run = True
    pause = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                elif event.key == pygame.K_p:
                    pause = not pause
        if not pause:
            game_clock.tick(50)  # framerate
            screen.blit(background.surface, (0, 0))
            [screen.blit(ue.figure, ue.get_next_location())
             for ue in user_equip]
            # pygame.display.update()
            pygame.display.flip()
        else:
            pygame.time.delay(1000)  # just delay 1 sec
    pygame.quit()


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

    @cli.command('run')
    @click.pass_context
    def run_game(ctx):
        """Start the game"""
        start_game(ctx.obj['n_moving_items'], ctx.obj['size_field'])

    cli(obj={})
    return True


# --------------------------------------------------


if __name__ == "__main__":
    get_arguments()
