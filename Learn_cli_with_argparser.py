"""Learn pass command arguments with 'argparse'."""

import time
import random
import argparse
import timeit


ABOUT = """
This program uses 'argparse' as command line parsers.
"""


def my_solver(filename: str) -> str:
    """Dummy solver function.
    It does nothing apart from waiting on average 2.5sec

    :argument filename: a string
    :return: the same filename a the input
    """
    print("Running my solver")
    time.sleep(random.random() * 2)
    return filename


def time_function(function_name: str, my_filename: str, n_retries: int = 20) -> True:
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
    average_time = meas_time / n_retries
    print(f"Average time of {function_name}: {average_time}s")
    return True


def get_arguments_with_argparse() -> True:
    """
    Examples using 'argparse'.
    The package argparse is 'standard' in the library
    :return: True
    """

    def config_argparse() -> argparse:
        """ This function configures 'argparse'
        :return: Argparse function
        """
        # Create instance of argparse (named 'parser')
        # Note that the help entries are used description of the arguments
        parser = argparse.ArgumentParser(description=ABOUT)
        # add options to 'parse'
        parser.add_argument('-s', '--solve',
                            help='Run solver',
                            action='store_true')
        parser.add_argument('-t', '--timing',
                            help='Run timer for each function',
                            action='store_true')
        parser.add_argument('filename',
                            help='Input filename')
        return parser.parse_args()

    # This command parses the input arguments!
    input_args = config_argparse()

    if input_args.solve is True:
        my_solver(input_args.filename)

    if input_args.timing is True:
        # call the 'timit' function
        time_function('my_solver', my_filename=input_args.filename)
        pass

    return True


# --------------------------------------------------


if __name__ == "__main__":
    get_arguments_with_argparse()
