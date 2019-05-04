#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv


with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'count']
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'A', 'count': '1'})
    writer.writerow({'name': 'B', 'count': '1'})

with open('test.csv', 'r',) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['name'], row['count'])
