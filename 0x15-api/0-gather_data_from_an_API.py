#!/usr/bin/python3
"""
    Simple API Call from JSONPlaceholder
"""


from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    api_link = 'https://jsonplaceholder.typicode.com'
    r = get(f'{api_link}/users/{user_id}')
    name = r.json().get('name')
    r = get(f'{api_link}/todos/?userId={user_id}&completed=true')
    todos = r.json()
    print(f'Employee {name} is done with tasks({len(todos)}/20):')
    for todo in todos:
        print(f'\t{todo.get("title")}')
