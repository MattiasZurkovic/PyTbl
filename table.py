__author__ = 'mattias'

from sys import stdout

global label_length

def new_columns(columns):
    for i in columns:
        length = len(i)
        stdout.write('+' + '=' * (length + 2) + '+')
    print('\r')

    for i in columns:
        line_pos = ' |'
        stdout.write('| ' + i + line_pos)
    print('\r')

    for i in columns:
        length = len(i)
        stdout.write('+' + '=' * (length + 2) + '+')
    print('\r')

    for i in columns:
        return len(i)


def add_row(input):
    for x in input:
        stdout.write('| ' + x + ' |')
    print('\r')
    for x in input:
        length = len(x)
        stdout.write('+' + '-' * (length + 2) + '+')
    print('\r')



new_columns(['Animal', 'Damage Count', 'Name  '])
add_row(['Bear  ', '2000        ', 'Po    '])
add_row(['Cat   ', '3           ', 'Mew   '])
add_row(['Dog   ', '-10         ', 'Hunter'])

