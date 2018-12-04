"""
## SPIRAL PRINTING

Print 2-D array (nxm) in spiral order (clockwise)

INPUT:

1 2 3            Order goes in this format   1 2 3  next 6 9 next 7 8 next 4 5.
4 5 6
7 8 9

OUTPUT:

1 2 3 6 9 8 7 4 5


Execution: python spiral_order_clockwise.py spiral_order_input.txt

"""

import os
import sys
import itertools


def matrix_transpose_and_yield_top(matrix):
    """
    :param matrix:
    :return: yield from the top matrix
    """
    while matrix:
        yield matrix[0]
        matrix = list(reversed(list(zip(*matrix[1:]))))


def spiral_printing(file_path):
    """
    :param file_path:
    :return: spiral printing from the top
    """
    matrix = []
    with open(file_path, 'r') as opened_file:
        for line in opened_file:
            matrix.append(list(map(int, line.split(' '))))
    print(list(itertools.chain(*matrix_transpose_and_yield_top(matrix))))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if os.path.isfile(file_path):
            spiral_printing(file_path)
        else:
            print("File path not exists.\n")
