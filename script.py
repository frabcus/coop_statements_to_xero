#!/usr/bin/python

import csv
import sys
import re

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)

headers = None
for row in reader:
    if len(row) == 0:
	continue

    if not headers and re.match(" Date", row[0]):
        headers = row
        headers.append('Credit-Debit')

    elif re.match("\d\d/\d\d/\d\d\d\d", row[0]):
        if not headers:
            raise Exception("There are no headers")

        vals = dict(zip(headers, row))
        row.append(float(vals['Credit'] or 0) - float(vals['Debit'] or 0))

        writer.writerow(row)



