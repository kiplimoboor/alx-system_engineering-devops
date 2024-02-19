#!/usr/bin/python3
"""
    Simple API Call from JSONPlaceholder,
    And writing to csv file
"""


import csv
from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    api_link = 'https://jsonplaceholder.typicode.com'
    r = get(f'{api_link}/users/{user_id}')
    name = r.json().get('name')
    r = get(f'{api_link}/todos/?userId={user_id}')
    todos = r.json()

    with open('USER_ID.csv', 'w') as csvfile:
        fieldnames = ['userId', 'name', 'completed', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for todo in todos:
            writer.writerow({'userId': user_id,
                             'name': name,
                             'completed': todo.get('completed'),
                             'title': todo.get('title')})
