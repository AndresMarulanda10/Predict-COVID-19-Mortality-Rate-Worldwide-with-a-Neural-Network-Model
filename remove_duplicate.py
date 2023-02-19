#!/usr/bin/env python
# coding=utf-8
# remove_duplicate.py

import csv
import sys

if __name__ == '__main__':
    infile = sys.stdin
    outfile = sys.stdout
    if len(sys.argv) > 1:
        infile = open(sys.argv[1], 'r')
    
    reader = csv.reader(infile, delimiter=',', quotechar='"', 
                        quoting=csv.QUOTE_ALL, skipinitialspace=True)
    writer = csv.writer(outfile, delimiter=',', quotechar='"', 
                        quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    unique_rows = set()
    for row in reader:
        if tuple(row) not in unique_rows:
            unique_rows.add(tuple(row))
            writer.writerow(row)
