#! /usr/bin/env python
# coding=utf-8
# inner_join.py

import csv
import sys

if __name__ == '__main__':
    left_table_in = sys.stdin
    right_table_in = open(sys.argv[1], 'rb')
    outfile = sys.stdout

    left_reader = csv.reader(left_table_in, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    right_reader = csv.reader(right_table_in, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    left_key = None
    right_key = None

    try:
        left_row = next(left_reader)
        right_row = next(right_reader)
        while True:
            if left_key is None:
                left_key = (left_row[0], left_row[2])
            if right_key is None:
                right_key = (right_row[0], right_row[1])

            if left_key < right_key:
                left_row = next(left_reader)
                left_key = (left_row[0], left_row[2])
            elif left_key > right_key:
                right_row = next(right_reader)
                right_key = (right_row[0], right_row[1])
            else:
                row = left_row + [right_row[2]]
                writer.writerow(row)
                left_row = next(left_reader)
                right_row = next(right_reader)
                left_key = right_key = None

    except StopIteration:
        pass
