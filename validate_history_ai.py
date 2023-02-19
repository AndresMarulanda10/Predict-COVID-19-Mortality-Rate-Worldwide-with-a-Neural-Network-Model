#! /usr/bin/python
# coding=utf-8
# validate_history_ai.py

import csv
import sys

def validate_row(row):
    # check if the number of columns is right
    if len(row) != 12:
        return False
    # check the format of each column...skipped.
    # check the value range of each column...skipped.
    return True

if __name__ == '__main__':
    infile = sys.stdin
    outfile = sys.stdout

    reader = csv.reader(infile, delimiter=',', quotechar='"', 
                        quoting=csv.QUOTE_ALL, skipinitialspace=True)
    writer = csv.writer(outfile, delimiter=',', quotechar='"', 
                        quoting=csv.QUOTE_ALL, skipinitialspace=True)

    for row in reader:
        if validate_row(row):
            writer.writerow(row)
