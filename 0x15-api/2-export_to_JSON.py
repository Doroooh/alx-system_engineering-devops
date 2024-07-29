#!/usr/bin/python3

"""
The Python script to export data in JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    employeedata = response.json()

    therow = []
    secondresponse = get('https://jsonplaceholder.typicode.com/users')
    emplsecdata = secondresponse.json()

    for t in emplsecdata:
        if t['id'] == int(argv[1]):
            u_name = t['username']
            id_no = t['id']

    therow = []

    for t in employeedata:

        newdictn = {}

        if t['userId'] == int(argv[1]):
            newdictn['username'] = u_name
            newdictn['task'] = t['title']
            newdictn['completed'] = t['completed']
            therow.append(newdictn)

    enddict = {}
    enddict[id_no] = therow
    json_obj = json.dumps(enddict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
