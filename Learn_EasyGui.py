"""Learn EasyGUI: file selection, errors, choices and demos"""

import os
import sys
import easygui as eg
import click

ABOUT = """Learn and examples with EasyGUI"""
TITLE = """Learn EasyGUI"""


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
    eg.msgbox(title=TITLE+": Example Error",
              image=os.path.join('Images', 'failure.gif'),
              msg=error_string)
    return True


def select_file() -> True:
    """Use EasyGUI to select a function"""
    current_directory = os.getcwd()
    selected_file = eg.fileopenbox(title=TITLE+': Open a file',
                                   default=os.path.join(current_directory, ".."),
                                   filetypes="*.txt,*.py")
    print(f"Selected file: {os.path.basename(selected_file)}")
    print(f"In directory: {os.path.dirname(selected_file)}")
    return True


def message_box(message: str) -> True:
    message += "\n\nFor resources see:  https://pythonhosted.org/easygui/index.html"
    eg.msgbox(title=TITLE+": message",
              msg=message,
              ok_button='OK',
              image=os.path.join('Images', 'Learn.png'))
    return True


def user_choices() -> True:
    """
    The user selects an action
    :return: True
    """
    message_box("EasyGUI examples.\n\nThis is a message box.\n\t\t\tAuthor: XX")

    # This is a 'clever' technique!
    # Define the strings you need to use in a dictionaty,
    # and associate each string to a function name
    all_choices = {'Run my\nfunction': my_function,
                   'Select a\nfile': select_file,
                   'Show the demo': eg.egdemo}

    # Use Gui to select a choice
    choice = eg.buttonbox(msg="Select and action",
                          title=TITLE+': choice',
                          choices=list(all_choices.keys()),
                          image=os.path.join('Images', 'qm.png'))

    # This is the clever bit!! Run the choice as a function
    all_choices[choice]()
    return True


# --------------------------------------------------


if __name__ == "__main__":
    @click.group(help=ABOUT)
    def cli():
        """Main call to the CLI"""
        pass

    @cli.command('test', help="test a specific part of the code", hidden=True)
    def test_code():
        my_function()
        sys.exit()

    cli(obj={})
    # Run my function
    user_choices()
