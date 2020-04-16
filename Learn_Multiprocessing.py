"""Learn spawning different processes in python, using Multiprocessing"""


import multiprocessing
import time
import timeit
import random
import click


ABOUT = """
This program compares serially call a function versus parallelize the function calls.
Parallelization uses the 'multiprocessing' standard library. 
It should work both in Linux and Windows
"""


def my_calls(call_number: int) -> str:
    """Dummy call function.
    It does nothing apart from waiting on average 2sec

    :Return: the same filename a the input
    """
    delay = random.random() * 2
    time.sleep(delay)
    print(f"my_call #{call_number} has terminated")
    return round(delay, 3)


def parallel_calls(n_calls: int) -> True:
    """
    Call the function in parallel
    :param n_calls: number of time to call the function
    :return: True
    """
    print(f"Call my_call in parallel {n_calls} times")
    with multiprocessing.Pool(n_calls) as mpp:
        delay = mpp.map(my_calls, range(n_calls))
    print(delay)


def iter_calls(n_calls: int) -> True:
    """
    Call the function in sequence
    :param n_calls: number of time to call the function
    :return: True
    """
    print(f"Call my_call iteratively {n_calls} times")
    delay = []
    for cnt in range(n_calls):
        delay.append(my_calls(cnt))
    print(delay)


def timing_function(function_to_time: str, n_calls: int) -> True:
    """
    Time the 'iter_calls'
    :param function_to_time: name of the function to time
    :param n_calls: number of time to call the function
    :return: True
    """
    print(f"*** Start timing the function {function_to_time}")
    n_retry = 6
    measured_time = timeit.timeit(f"{function_to_time}({n_calls})",
                                  setup=f"from __main__ import {function_to_time}",
                                  number=n_retry)
    average_time = round(measured_time / n_retry, 2)
    print(f"Function run by {function_to_time} takes {average_time} seconds.")
    return True


def get_arguments() -> True:
    """ Use click to get command line arguments

    :return: True
    """
    max_n_calls = 1e5
    default_n_calls = 5

    @click.group(help=ABOUT)
    @click.option('--n_calls', '-n', default=default_n_calls,
                  type=click.IntRange(1, max_n_calls),
                  help='Number of calls to the "my_calls" function.\n' +
                  f"DEFAULT: {default_n_calls}; RANGE: [1, {max_n_calls}]")
    @click.pass_context
    def cli(ctx, n_calls):
        """Entry to the CLI"""
        ctx.obj['n_calls'] = n_calls

    @cli.command(help='Call solver iteratively')
    @click.pass_context
    def time_iter(ctx):
        """Call the timine to the iterator function"""
        timing_function('iter_calls', ctx.obj['n_calls'])

    @cli.command(help='Call solver in parallel')
    @click.pass_context
    def time_parallel(ctx):
        """Call the timing of the parallelized function"""
        timing_function('parallel_calls', ctx.obj['n_calls'])

    cli(obj={})


def main():
    get_arguments()


# --------------------------------------------------


if __name__ == "__main__":
    main()
