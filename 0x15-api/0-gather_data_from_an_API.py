#!/usr/bin/python3
"""
    Simple API usage in Python with requests
"""

from requests import get
from sys import argv

user_id = argv[1]
api_link = 'https://jsonplaceholder.typicode.com'
r = get(f'{api_link}/users/{user_id}')
name = r.json()['name']
r = get(f'{api_link}/todos/?userId={user_id}&completed=true')
todos = r.json()

print(f'Employee {name} is done with tasks({len(todos)}/20):')
for todo in todos:
    print(f'\t{todo["title"]}')
