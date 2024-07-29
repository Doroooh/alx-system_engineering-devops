#!/usr/bin/python3

"""
This Python script uses the REST API for an employee ID to return data on the progress of the todo list.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    employeedata = response.json()
    completed = 0
    totlvalue = 0
    todo = []
    secondresponse = get('https://jsonplaceholder.typicode.com/users')
    employeedatatwo = secondresponse.json()

    for t in employeedatatwo:
        if t.get('id') == int(argv[1]):
            employee = t.get('name')

    for t in employeedata:
        if t.get('userId') == int(argv[1]):
            totlvalue += 1

            if t.get('completed') is True:
                completed += 1
                todo.append(t.get('title'))

    print("Employee {} is done with todo({}/{}):".format(employee, completed,
                                                          totlvalue))

    for t in todo:
        print("\t {}".format(t))
