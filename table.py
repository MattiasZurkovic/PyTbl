__author__ = 'mattias'

from sys import stdout

def new(columns):
    for i in columns:
        length = len(i)
        stdout.write('-' * (length + 8))
    print('\r')
    for i in columns:
        stdout.write('|   ' + i + '   |')
    print('\r')
    for i in columns:
        length = len(i)
        stdout.write('-' * (length + 8))
    print('\r')


def add_row(input):
    for x in input:
        stdout.write('|   ' + x + '   |')

new(['Animal', 'Danger'])
add_row(['Bear', 'Yes'])