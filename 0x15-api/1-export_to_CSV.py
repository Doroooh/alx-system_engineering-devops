#!/usr/bin/python3

"""
 data export CSV format
"""
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    responsetwo = get('https://jsonplaceholder.typicode.com/users')
    datatwo = responsetwo.json()

    for k in datatwo:
        if k['id'] == int(argv[1]):
            employee = k['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for k in data:

            row = []
            if k['userId'] == int(argv[1]):
                row.append(k['userId'])
                row.append(employee)
                row.append(k['completed'])
                row.append(k['title'])

                writ.writerow(row)
