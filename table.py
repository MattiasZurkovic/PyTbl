__author__ = 'mattias'

from sys import stdout

def new(columns):
    for i in columns:
        length = len(i)
        stdout.write('-' * (length + 6))
        stdout.write('|   ' + i + '   |')


def add_row(input):
    for x in input:
        stdout.write('|   ' + x + '   |')


new(['Weapon', 'Damage'])