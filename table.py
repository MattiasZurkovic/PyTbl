__author__ = 'mattias'

from sys import stdout

global label_length
global label_style



def new_columns(columns, style):
    if style == 1:
        label_style = '='
    elif style == 2:
        label_style = '~'
    elif style == 3:
        label_style = '-'
    elif style == 4:
        label_style = '#'
    elif style == 5:
        label_style = '▬'
    elif style == 6:
        label_style = '▫'
    else:
        label_style = '='

    for i in columns:
        length = len(i)
        stdout.write('+' + label_style * (length + 2) + '+')
    print('\r')

    for i in columns:
        line_pos_right = ' |'
        stdout.write('| ' + i + line_pos_right)
    print('\r')

    for i in columns:
        stdout.write('+' + label_style * (length + 2) + '+')
    print('\r')


# Add a row - this method adds a row to the table
def add_row(input):
    for x in input:
        input_length = len(x)
        stdout.write('| ' + x + ' |')
    print('\r')
    for x in input:
        length = len(x)
        stdout.write('+' + '-' * (length + 2) + '+')
    print('\r')



def add_column(column_title, column_data):
    for m in column_title:
        length = len(m)
        stdout.write('+' + '=' * (length + 2) + '+')
    print('\r')

    for m in column_title:
        line_pos_right = ' |'
        stdout.write('| ' + m + ' |')
    print('\r')

    for m in column_title:
        stdout.write('+' + '=' * (length + 2) + '+')
    print('\r')
# ----------------------------------------------------
    for m in column_data:
        this_length = len(m)

        if this_length < length:
            wanted_l = length - this_length
        elif this_length > length:
            wanted_l = this_length - length

        stdout.write('| ' + m + ' ' * (wanted_l) + ' |')
    print('\r')


add_column(['Animal'], ['Hello', 'Cat'])

