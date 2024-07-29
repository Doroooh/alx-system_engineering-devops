#!/usr/bin/python3

"""
in this python script, there will be data export CSV format
"""
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    employeedata = response.json()

    therow = []
    secondresponse = get('https://jsonplaceholder.typicode.com/users')
    emplsecdata = secondresponse.json()

    for t in emplsecdata:
        if t['id'] == int(argv[1]):
            employee = t['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for t in employeedata:

            therow = []
            if t['userId'] == int(argv[1]):
                therow.append(t['userId'])
                therow.append(employee)
                therow.append(t['completed'])
                therow.append(t['title'])

                writ.writerow(row)
