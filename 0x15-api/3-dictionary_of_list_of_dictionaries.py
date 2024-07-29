#!/usr/bin/python3

"""Exporting data in JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    a_users = requests.get("https://jsonplaceholder.typicode.com/users")
    a_users = a_users.json()
    todolist = requests.get('https://jsonplaceholder.typicode.com/todos')
    todolist = todolist.json()
    todotasksAll = {}

    for a_user in a_users:
        todoLists = []
        for todo in todolist:
            if todo.get('userId') == a_user.get('id'):
                todoDict = {"username": a_user.get('username'),
                            "task": todo.get('title'),
                            "completed": todo.get('completed')}
                todoLists.append(todoDict)
        todotasksAll[a_user.get('id')] = todoLists

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todotasksAll, f)
