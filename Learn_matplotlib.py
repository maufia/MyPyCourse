"""Learn matplotlib"""


import os
import easygui as eg
import csv
import matplotlib.pyplot as plt
import click

TITLE = "Learn - Matplotlib"


def select_file() -> str:
    """Use EasyGUI to select a function"""
    current_directory = os.path.join(os.getcwd(), 'Data')
    selected_file = eg.fileopenbox(title=f'{TITLE}: Open a file',
                                   default=os.path.join(current_directory, ".."),
                                   filetypes="*.txt")
    print(f"Selected file: {os.path.basename(selected_file)}")
    print(f"In directory: {os.path.dirname(selected_file)}")
    return selected_file


def read_file(data: dict) -> dict:
    """
    Read the file. Save the original into the input data dictionary.

    :param data: dictionary for passing data
    :return: a data structure with data

    >>> data= {'orig': {'filename': os.path.join('Data', 'trends_cupcakes.csv')}}
    >>> read_file(data)['orig']['Name time-line']
    'Month'
    >>> read_file(data)['orig']['Name values']
    'Cupcake: (Worldwide)'
    """
    data['orig']['time'] = []
    data['orig']['values'] = []
    with open(data['orig']['filename']) as csvfile:
        for row_count, row in enumerate(csv.reader(csvfile, delimiter=',')):
            if not row:
                continue
            if row_count == 0:
                data['orig']['category'] = row[0]
                continue
            if row_count == 2:
                data['orig']['Name time-line'] = row[0]
                data['orig']['Name values'] = row[1]
            else:
                data['orig']['time'].append(row[0])
                data['orig']['values'].append(row[1])
    return data


def display_original_data(data: dict) -> True:
    """
    Display data

    :param data: data set to display needs 'time' and 'values'
    :return: True
    """
    time = range(len(data['orig']['time']))
    fig, ax = plt.subplots()
    ax.plot(time, data['orig']['values'], '.b')
    ax.set(xlabel='time [months]', ylabel='Number of searches',
           title=f"Analysis of searches for {data['orig']['Name values']}")
    ax.grid()
    plt.show()
    return True


def display_analyse_data(data: dict) -> dict:
    return data


def select_operation(data) -> True:
    """"""
    all_choices = {'Display\noriginal\ndata': display_original_data,
                   'Display\nanalysed\ndata': display_analyse_data}
    # Use Gui to select a choice
    choice: str = eg.buttonbox(msg="Select what to display",
                               title=TITLE,
                               choices=list(all_choices.keys()),
                               image=os.path.join('Images', 'qm.png'))

    assert choice in all_choices, show_error_message('The choice is not available')
    # This is the clever bit!! Run the choice as a function
    all_choices[choice](data)
    return True


def message_box(message: str) -> True:
    eg.msgbox(title=TITLE,
              msg=message,
              ok_button='OK',
              image=os.path.join('Images', 'Learn.png'))
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


def main() -> True:
    # Initialse the data set
    data = {'orig': {'filename': ""}, 'analysis': {}}
    message_box("First select a data file")
    data['orig']['filename'] = select_file()
    data = read_file(data)
    select_operation(data)
    return True


# --------------------------------------------------


if __name__ == "__main__":
    @click.group(help=TITLE)
    def cli():
        pass

    @cli.command('run', help='Run full program')
    def cli_run():
        main()

    @cli.command('test', help='Test csv testing')
    def cli_test():
        import doctest
        failures_count, test_count = doctest.testmod(verbose=False)
        assert failures_count == 0, 'Test failure... bailing out'
        print(f'All {test_count} tests passed')

    cli(obj={})
