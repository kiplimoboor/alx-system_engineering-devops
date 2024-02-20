#!/usr/bin/python3
"""
    Simple API Call from JSONPlaceholder,
    And writing to JSON file
"""


import json
from requests import get

if __name__ == "__main__":
    api_link = "https://jsonplaceholder.typicode.com"
    users = get(f"{api_link}/users").json()
    todos = get(f"{api_link}/todos").json()
    filename = 'todo_all_employees.json'

    all_todos = {}
    for user in users:
        user_todos = []
        id = user.get('id')
        username = user.get('username')
        for todo in todos:
            if todo.get('userId') == id:
                user_todos.append({
                    'username': username,
                    'task': todo.get('title'),
                    'completed': todo.get('completed')
                    })
        all_todos[str(id)] = user_todos

    with open(filename, 'w') as jsonfile:
        json.dump(all_todos, jsonfile)
