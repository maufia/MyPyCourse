"""Learn PyGame package with few examples"""


import click
import pygame


def start_game() -> True:
    """ Set up pygame
    :return: True
    """
    pygame.init()
    size = width, length = 600, 600
    speed[2, 2]
    screen = pygame.display.set_mode(size)

    return True


def get_arguments() -> True:
    """
    Get arguments from command line
    :return: True
    """
    @click.group()
    def cli():
        pass

    @cli.command()
    def run_game():
        start_game()

    cli({})
    return True


# --------------------------------------------------


if __name__ == "__main__":
    get_arguments()
