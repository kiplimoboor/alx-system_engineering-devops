#!/usr/bin/python3
"""
    A simple module to make API Calls
    To a mockup API server and return the
    Responses. Then print them out to standard output
    Usage: ./0-gather-data_from_an_API <ID>
    Where <ID> is the employee ID for whom we want to list
    The tasks
"""

from requests import get
from sys import argv

user_id = argv[1]
api_link = 'https://jsonplaceholder.typicode.com'
r = get(f'{api_link}/users/{user_id}')
name = r.json().get('name')
r = get(f'{api_link}/todos/?userId={user_id}&completed=true')
todos = r.json()

print(f'Employee {name} is done with tasks({len(todos)}/20):')
for todo in todos:
    print(f'\t{todo.get("title")}')
