"""Learn read/wrtire to excell spreadsheet"""

from openpyxl import load_workbook, Workbook
from datetime import date


today_date = date.today()


def my_function() -> dict:
    """Function creates a set of data into a dictionary"""
    hills_of_rome = {
           'Aventine Hill': {'Latin': 'Aventinus',
                             'Hights': 46.6,
                             'Italian': 'Aventino'},
           'Caelian Hill': {'Latin': r'Cælius',
                            'Hights': 50.0,
                            'Italian': 'Celio'},
           'Capitoline Hill': {'Latin': 'Capitolinus',
                               'Hights': 44.7,
                               'Italian': 'Campidoglio'},
           'Esquiline Hill': {'Latin': 'Esquilinus',
                              'Hights': 58.3,
                              'Italian': 'Esquilino'},
           'Palatine Hill': {'Latin': 'Palatinus',
                             'Hights': 51.0,
                             'Italian': 'Palatino'},
           'Quirinal Hill': {'Latin': 'Quirinalis',
                             'Hights': 50.9,
                             'Italian': 'Quirinale'},
           'Viminal Hill': {'Latin': 'Viminalis',
                             'Hights': 57.0,
                             'Italian': 'Viminale'}}
    return hills_of_rome


def write_to_spreadsheet(filename: str, hills_of_rome: dict) -> True:
    """
    Write the dictionary to spreadsheet

    :param filename: string filename
    :param hills_of_rome: dictionary with hills of rome

    return: True
    """
    # open workbook in memory
    workbook = Workbook()
    # Createa history sheet named 'History'

    sheet = workbook.create_sheet(title='History')
    # Write to cell
    sheet['A1'] = 'Date'
    sheet['A2'] = today_date.strftime("%d/%m/%Y")
    sheet['B1'] = 'Author'
    sheet['B2'] = 'Julius Caesar'

    # Createa sheet named 'Hills'
    sheet = workbook.create_sheet(title='Hills')
    # Create the first row with headings
    headings = ['English Name', 'Italian Name', 'Latin Name', 'Height [m]']
    # for each pattern name write to a column
    for column, heading in enumerate(headings):
        column = column + 1    # excell starts counting from 1
        # Write the name of the patten in row 1
        sheet.cell(row=1, column=column).value = heading

    # for each domains discovered in the search (also sorted)
    for row_count, hill in enumerate(sorted(hills_of_rome)):
        # write the hill in subsequent rows (same column as above)
        sheet.cell(row=row_count+2, column=1).value = hill
        sheet.cell(row=row_count+2, column=2).value = \
                hills_of_rome[hill]['Italian']
        sheet.cell(row=row_count+2, column=3).value = \
                hills_of_rome[hill]['Latin']
        sheet.cell(row=row_count+2, column=4).value = \
                hills_of_rome[hill]['Hights']
    # delete default Sheet
    del workbook["Sheet"]
    print("\nWriting to file")
    # Write workbook to file
    workbook.save(filename)


def read_spreadsheet(filename: str) -> dict:
    """
    Read the dictionary to spreadsheet

    :param filename: string filename
    :param hills_of_rome: dictionary with hills of rome

    return: True
    """
    pass


def main():
    hills_of_rome = my_function()
    filename = 'hills_of_rome.xlsx'
    write_to_spreadsheet(filename, hills_of_rome)
    hor = read_spreadsheet(filename)
    print(hor)


# --------------------------------------------------


if __name__ == "__main__":
    main()
