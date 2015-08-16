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
        line_pos = ' |'
        stdout.write('| ' + i + line_pos)
    print('\r')

    for i in columns:
        length = len(i)
        stdout.write('+' + label_style * (length + 2) + '+')
    print('\r')




# Add a row - this method adds a row to the table
def add_row(input):
    for x in input:
        stdout.write('| ' + x + ' |')
    print('\r')
    for x in input:
        length = len(x)
        stdout.write('+' + '-' * (length + 2) + '+')
    print('\r')



new_columns(['Animal', 'Damage Count', 'Name  '], 1)
add_row(['Bear  ', '2000        ', 'Po    '])
add_row(['Cat   ', '3           ', 'Mew   '])
add_row(['Dog   ', '-10         ', 'Hunter'])

