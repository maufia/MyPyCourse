"""Learn basics of logging"""


import os
import logging


FUNC_NAME = "MyFunction"


def my_function() -> True:
    """Any generic function"""
    logger = logging.getLogger("My Function")
    logger.info("My function was called")
    for i in range(5):
        logger.info(f"Obtained number {i}")
    return


def setup_logging(working_dir: str, log_file_name: str = 'logfile.log') -> bool:
    """
    Set up logging instance
    :return:  True
    """
    log_file = os.path.join(working_dir, log_file_name)
    FORMAT = '%(asctime)s | %(name)s | %(message)s'
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        filemode='w', format=FORMAT,
                        datefmt='%Y-%m-%d %H:%M')
    return True


def main() -> True:
    """Main for Learn Logging"""
    working_dir = os.getcwd()
    setup_logging(working_dir, 'MyFunction.log')
    logger = logging.getLogger("Main")
    logger.info("Main is started started")
    logger.info(f"Working dir: {working_dir}")
    my_function()
    logger.info("Returned to main")
    return True


# --------------------------------------------------


if __name__ == "__main__":
    main()
