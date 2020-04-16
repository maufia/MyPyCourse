""""Learn pass command arguments with 'click'."""

import time
import random
import timeit
import click

ABOUT = """
This program uses 'click' as command line parsers.
It must be provided with:
Filename: a string

Documentation:  https://click.palletsprojects.com
"""


def my_solver(filename: str) -> str:
    """Dummy solver function.
    It does nothing apart from waiting on average 2.5sec

    :type filename: object
    :Return: the same filename a the input
    """
    print("Running my solver")
    time.sleep(random.random() * 2)
    return filename


def time_function(function_name: str, my_filename: str, n_retries: int = 10) -> True:
    """
    Timing function

    :param my_filename: the string to be passed to my_solver
    :param function_name: Name of function to be timed
    :param n_retries: Number of times the function is run to improve the average
    :return: True
    """
    meas_time = timeit.timeit(f"{function_name}('{my_filename}')",
                              setup="from __main__ import " + function_name,
                              number=n_retries, globals=globals())
    average_time = round(meas_time / n_retries, 2)
    print(f"Average time of {function_name}: {average_time}s")
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
    @click.option('--n_retries', '-n', default=5,
                  type=click.IntRange(1, 1e6),
                  help='Number of retries for timing operation.\n' +
                       'DEFAULT=100, RANGE=[1..1E6]')
    @click.pass_context
    def timing(ctx, n_retries):
        """Call the timing function"""
        click.echo(f'Timing {ctx.obj["filename"]} with {n_retries} retries')
        time_function('my_solver', ctx.obj["filename"], n_retries)

    @cli.command(help='Runs solver')
    @click.pass_context
    def solve(ctx):
        """Call the solving function"""
        my_solver(ctx.obj['filename'])

    # call command line interface parser:
    cli(obj={})


# --------------------------------------------------


if __name__ == "__main__":
    get_arguments_with_click()
