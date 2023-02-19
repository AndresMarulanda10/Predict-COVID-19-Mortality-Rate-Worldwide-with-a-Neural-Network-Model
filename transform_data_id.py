#! /usr/bin/python
# coding=utf-8
# transform_data_id.py

import csv
import sys
import traceback


def load_data_object_ids(cfgfile):
    """Load data object ids from a configuration file."""
    data_object_ids = {}
    cfgreader = csv.reader(cfgfile, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in cfgreader:
        try:
            key = int(row[0]), int(row[1])
            value = int(row[2])
            data_object_ids[key] = value
        except ValueError:
            pass
    return data_object_ids


if __name__ == '__main__':
    infile = sys.stdin
    outfile = sys.stdout
    cfgfile = None

    if len(sys.argv) > 1:
        cfgfile = open(sys.argv[1], 'r', encoding='utf-8')

    data_object_ids = load_data_object_ids(cfgfile)

    reader = csv.reader(infile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_ALL, skipinitialspace=True)
    writer = csv.writer(outfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_ALL, skipinitialspace=True)

    for row in reader:
        try:
            key = int(row[0]), int(row[2])
            data_id = data_object_ids.get(key, None)
            if data_id is not None:
                converted = [data_id, row[1]]
                converted.extend(row[3:])
                writer.writerow(converted)
        except:
            print(row, traceback.format_exc(), file=sys.stderr)
