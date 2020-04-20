"""Learn matplotlib"""


import os
import easygui as eg
import csv
import matplotlib.pyplot as plt


TITLE = """Learn - Matplotlib """


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
    data['orig']['x'] = []
    data['orig']['values'] = []
    with open(data['orig']['filename']) as csvfile:
        for row_count, row in enumerate(csv.reader(csvfile, delimiter=',')):
            if not row:
                continue
            if row_count == 0:
                data['orig']['category'] = row[0]
                continue
            if row_count == 2:
                data['orig']['Name x-line'] = row[0]
                data['orig']['Name values'] = row[1]
            else:
                data['orig']['x'].append(row[0])
                try:
                    data['orig']['values'].append(int(row[1]))
                except ValueError:
                    data['orig']['values'].append(0)
    return data


def display_original_data(data: dict) -> True:
    """
    Display data

    :param data: data set to display needs 'time' and 'values'
    :return: True

    >>> data= {'orig': {'filename': os.path.join('Data', 'trends_cupcakes.csv')}}
    >>> data = read_file(data)
    >>> display_original_data(data)
    True
    """
    time = range(len(data['orig']['x']))
    # open figure
    fig = plt.figure()
    fig.suptitle(f"Analysis of searches for {data['orig']['Name values']}")
    # set up 2 subplots
    ax = fig.subplots(nrows=2, ncols=1)
    # first subplot
    ax[0].plot(time, data['orig']['values'], '.b')
    ax[0].set(xlabel='time [months]', ylabel='Number of searches',
              title='Searches per number of months')
    ax[0].grid()

    # second plot
    ax[1].plot(time, data['orig']['values'], '.r')
    ax[1].set_xlabel('time [months]')
    ax[1].set_ylabel('Number of searches')
    ax[1].set_title('Searches per number of months')
    ax[1].grid()
    # proper axis and ticks
    labels = ax[1].get_xticklabels()
    for cnt, xtick in enumerate(ax[1].get_xticks()[0:-2]):
        labels[cnt] = data['orig']['x'][int(xtick)]
    ax[1].set_xticklabels(labels)
    # Rotate the ticks
    for tick in ax[1].get_xticklabels():
        tick.set_rotation(55)
    # sort out
    fig.subplots_adjust(bottom=0.2, top=0.8, hspace=0.6)
    plt.show()
    return True


def display_per_nation(data: dict) -> True:
    all_countries = data['orig']['x']
    all_values = data['orig']['values']
    max_size = 70
    pie_labels, pie_sizes = [f'Rest of the World'], [0]
    for cnt, value in enumerate(all_values):
        if value >= max_size:
            pie_labels.append(all_countries[cnt])
            pie_sizes.append(value)
        else:
            pie_sizes[0] += value
    explode = [0.0 for _ in pie_sizes]
    maximum_size: int = pie_sizes.index(max(pie_sizes))
    explode[maximum_size] = .3

    fig1, ax1 = plt.subplots()
    fig1.suptitle(f"Analysis of searches for {data['orig']['Name values']}")
    ax1.pie(pie_sizes, labels=pie_labels, explode=explode,
            shadow=True, autopct='%1.1f%%')
    # ax1.axis('equal')    # Equal aspect ratio ensures that pie is drawn as a circle.

    fig2, ax2 = plt.subplots()
    fig2.suptitle(f"Analysis of searches for {data['orig']['Name values']}")
    ax2.barh(pie_labels, pie_sizes)
    ax2.set_yticks(range(len(pie_labels)))
    ax2.set_yticklabels(pie_labels)
    ax2.invert_yaxis()  # labels read top-to-bottom
    ax2.set_xlabel('Searches')
    fig2.subplots_adjust(left=0.2, right=1.0)

    plt.show()
    return True


def select_operation(data) -> True:
    """"""
    all_choices = {'Monthly trend': display_original_data,
                   'National data': display_per_nation}
    # Use Gui to select a choice
    choice: str = eg.buttonbox(msg="Select what to display", title=TITLE,
                               choices=list(all_choices.keys()),
                               image=os.path.join('Images', 'qm.png'))

    assert choice in all_choices, show_error_message('The choice is not available')
    # This is the clever bit!! Run the choice as a function
    all_choices[choice](data)
    return True


def message_box(message: str) -> True:
    message += "\n\nFor resources see: https://matplotlib.org/gallery "
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
    import click

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

    @cli.command('disp')
    def cli_disp():
        data = {'orig': {'filename': os.path.join('Data', 'geoMap_cupcakes.csv')}}
        data = read_file(data)
        display_per_nation(data)


    cli(obj={})
