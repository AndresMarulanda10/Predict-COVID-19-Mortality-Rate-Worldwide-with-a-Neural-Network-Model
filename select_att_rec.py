#!/usr/bin/env python
# coding=utf-8
# select_history_ai.py

import csv
import sys

if __name__ == '__main__':
    reader = csv.reader(sys.stdin, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    for row in reader:
        try:
            outrow = [row[0], row[2], row[3], row[4]]
            writer.writerow(outrow)
        except IndexError:
            continue
