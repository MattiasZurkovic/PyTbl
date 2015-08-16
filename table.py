__author__ = 'mattias'

from sys import stdout

def new(columns):
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


def add_row(input):
    for x in input:
        stdout.write('| ' + x + ' |')
    print('\r')
    for x in input:
        length = len(x)
        stdout.write('+' + '-' * (length + 2) + '+')
    print('\r')



new(['Animal', 'Damage Count'])
add_row(['Bear  ', '2000        '])
add_row(['Cat   ', '3           '])

