"""Learn matplotlib"""


import os
import easygui as eg
import matplotlib


TITLE = "Learn - Matplotlib"


def read_data() -> dict:
    return {}

def display_data() -> True:
    return True


def analyse_data() -> True:
    return True


def show_options() -> True:
    """"""
    all_choices = {'Display\ndata': display_data,
                   'Analyse\ndata': analyse_data}

    # Use Gui to select a choice
    choice = eg.buttonbox(msg="Select and action",
                          title=TITLE,
                          choices=list(all_choices.keys()),
                          image=os.path.join('Images', 'qm.png'))

    # This is the clever bit!! Run the choice as a function
    all_choices[choice]()
    return True


def select_file() -> str:
    """Use EasyGUI to select a function"""
    current_directory = os.getcwd()
    selected_file = eg.fileopenbox(title=f'{TITLE}: Open a file',
                                   default=os.path.join(current_directory, ".."),
                                   filetypes="*.txt")
    print(f"Selected file: {os.path.basename(selected_file)}")
    print(f"In directory: {os.path.dirname(selected_file)}")
    return selected_file


def message_box(message: str) -> True:
    eg.msgbox(title=TITLE,
              msg=message,
              ok_button='OK',
              image=os.path.join('Images','Learn.png'))
    return True

def main() -> True:
    message_box("First select a data file")
    filename = select_file()
    data = read_file(filename)

    return True

# --------------------------------------------------


if __name__ == "__main__":
    main()
