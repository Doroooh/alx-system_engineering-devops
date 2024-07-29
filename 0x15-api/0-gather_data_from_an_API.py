#!/usr/bin/python3

"""
Python script that utilizes an API to retrieve an employees to do with the employee ID
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    ttl = 0
    tasks = []
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
                tasks.append(k.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          ttl))

    for k in tasks:
        print("\t {}".format(k))
