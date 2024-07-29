#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    todotasks = []
    responsetwo = get('https://jsonplaceholder.typicode.com/users')
    datatwo = responsetwo.json()

    for k in datatwo:
        if k.get('id') == int(argv[1]):
            employee = k.get('name')

    for k in data:
        if k.get('userId') == int(argv[1]):
            total += 1

            if k.get('completed') is True:
                completed += 1
                todotasks.append(k.get('title'))

    print("Employee {} is done with todotasks({}/{}):".format(employee, completed,
                                                          total))

    for k in todotasks:
        print("\t {}".format(k))
