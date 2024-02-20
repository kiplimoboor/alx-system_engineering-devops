#!/usr/bin/python3
"""
    Simple API Call from JSONPlaceholder,
    And writing to JSON file
"""


import json
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    api_link = "https://jsonplaceholder.typicode.com"
    username = get(f"{api_link}/users/{user_id}").json().get("username")
    todos = get(f"{api_link}/todos/?userId={user_id}").json()
    filename = f'{user_id}.json'
    todos_array = []
    for todo in todos:
        todos_array.append({
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username,
        })

    with open(filename, 'w') as jsonfile:
        todos_dictionary = {f'{user_id}': todos_array}
        json.dump(todos_dictionary, jsonfile)
