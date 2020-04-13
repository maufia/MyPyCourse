"""Learn different command arguments."""

import time
import random
import argparse
import click

ABOUT = """
This program uses different command line parsers.
"""


def my_solver(filename: str) -> str:
    """Dummy solver function.
    It does nothing apart from waiting on average 2.5sec

    :type filename: object
    :Return: the same filename a the input
    """
    print("Running my solver")
    time.sleep(random.random() * 5)
    return filename


def get_arguments_with_argparse() -> True:
    """
    Examples with 'argparser'.
    The package argparse is 'standard' in the library
    :return: True
    """

    def config_argparse() -> argparse:
        """ Configuring 'argparse'
        :return: Argparse function
        """
        parser = argparse.ArgumentParser(description=ABOUT)
        parser.add_argument('-s', '--solve',
                            help='Run solver',
                            action='store_true')
        parser.add_argument('-t', '--timing',
                            help='Run timer for each function',
                            action='store_true')
        parser.add_argument('filename',
                            help='Input filename')
        return parser.parse_args()

    # Call parser
    input_args = config_argparse()

    if input_args.solve is True:
        my_solver(input_args.filename)

    if input_args.timeit is True:
        "left to the reader"
        pass

    return True


def get_arguments_with_click() -> True:
    """
    Examples with 'click'
    The package needs to be loaded with pip

    :return: True
    """

    @click.group(help=ABOUT)
    @click.argument('filename', type=click.STRING)
    @click.pass_context
    def cli(ctx, filename):
        """Entry to the CLI"""
        ctx.obj['filename'] = filename
        click.echo(f'Passed filename: {filename}')

    @cli.command(help='Runs timer for each function')
    @click.option('--n_retries', '-n', default=100,
                  type=click.IntRange(1, 1e6),
                  help='Number of retries for timing operation.\n' +
                       'DEFAULT=100, RANGE=[1..1E6]')
    @click.pass_context
    def timing(ctx, n_retries):
        """Call the timing function"""
        click.echo(f'Timing {ctx.obj["filename"]} with {n_retries}')

    @cli.command(help='Runs solver')
    @click.pass_context
    def solve(ctx):
        """Call the solving function"""
        my_solver(ctx.obj['filename'])

    cli(obj={})


# --------------------------------------------------


if __name__ == "__main__":
    # get_arguments_with_argparse()
    get_arguments_with_click()
