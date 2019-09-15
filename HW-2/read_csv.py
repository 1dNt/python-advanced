import csv
import os
import sys
from argparse import ArgumentParser


if __name__ == '__main__':

    #parser = ArgumentParser()
    #parser.add_argument('-r', '--r_file', type=str, required=False,
    #                    help='Enter CSV file name: <name>.csv')
    #parser.add_argument('-w', '--w_file', type=str, required=False,
    #                    help='Enter CSV file name: <name>.csv')

    #args = parser.parse_args()

    print(sys.argv)

    try:
        path = sys.argv[1]
        try:
            key = sys.argv[2]
        except IndexError:
            key = '-r'

        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except IndexError:
        print('PathError: Enter file name and key')

