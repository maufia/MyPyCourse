"""Learn EasyGUI"""

import os
import easygui as eg
import click

ABOUT = """Learn and examples with EasyGUI"""


def use_gui_to_select_file() -> True:
    """Use EasyGUI to select a function"""
    current_directory = os.getcwd()
    selected_file = eg.fileopenbox(title='Open a file',
                                   default=os.path.join(current_directory, ".."),
                                   filetypes="*.txt,*.py")
    print(f"Selected file: {os.path.basename(selected_file)}")
    print(f"In directory: {os.path.dirname(selected_file)}")
    return True


def show_error_message() -> True:
    """
    A message box can be used for alert of error, success, etc
    return: True
    """
    eg.msgbox(title="Example Error",
              image=os.path.join('Images', 'failure.gif'),
              msg='Error message!\n\n No no no and no!')
    return True


def show_demos() -> True:
    """
    call Easy Gui demo, all type of widgets are shown
    :return: True
    """
    eg.egdemo()


def input_argument_handler():
    @click.group(help=ABOUT)
    def cli():
        """Main call to the CLI"""
        pass

    @cli.command(help="Open a file")
    def select_file():
        """Call select file"""
        use_gui_to_select_file()

    @cli.command(help="Error message")
    def error_message():
        """Call error message"""
        show_error_message()

    @cli.command(help="EasyGui demos")
    def all_demos():
        """Call easygui demos"""
        show_demos()

    cli(obj={})


# --------------------------------------------------


if __name__ == "__main__":
    input_argument_handler()
