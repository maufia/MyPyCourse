"""Learn EasyGUI"""

import os
import easygui as eg
import click

ABOUT = """Learn and examples with EasyGUI"""


def my_function() -> True:
    """Call error message
    :return: True
    """
    print("You have call me!")
    show_error_message("The function 'my_function' has raised and error")
    return True


def show_error_message(error_string="Error!") -> True:
    """
    A message box can be used for alert of error, success, etc
    return: True
    """
    eg.msgbox(title="Learn_EasyGUI: Example Error",
              image=os.path.join('Images', 'failure.gif'),
              msg=error_string)
    return True


def select_file() -> True:
    """Use EasyGUI to select a function"""
    current_directory = os.getcwd()
    selected_file = eg.fileopenbox(title='Learn_EasyGUI: Open a file',
                                   default=os.path.join(current_directory, ".."),
                                   filetypes="*.txt,*.py")
    print(f"Selected file: {os.path.basename(selected_file)}")
    print(f"In directory: {os.path.dirname(selected_file)}")
    return True


def input_argument_handler():
    @click.group(help=ABOUT)
    def cli():
        """Main call to the CLI"""
        pass

    @cli.command('choices', help="Select an option")
    def handle_choices() -> True:
        """
        Selects an option from list, and call a related functionality
        :return: True
        """
        # This is a 'clever' technique!
        # Define the strings you need to use in a dictionaty,
        # and associate each string to a function name
        all_choices = {'Run my\nfunction': my_function,
                       'Select a\nfile': select_file}

        # Use Gui to select a choice
        choice = eg.buttonbox(msg="Select and action",
                              title='Learn_EasyGui',
                              choices=list(all_choices.keys()),
                              image=os.path.join('Images', 'qm.png'))

        # This is the clever bit!! Run the choice as a function
        all_choices[choice]()
        return True

    @cli.command('demos', help="EasyGui demos")
    def show_demos():
        """Call easygui demos"""
        eg.egdemo()

    cli(obj={})


# --------------------------------------------------


if __name__ == "__main__":
    input_argument_handler()
