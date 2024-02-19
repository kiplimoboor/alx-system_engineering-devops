#!/usr/bin/python3
"""
    Simple API Call from JSONPlaceholder,
    And writing to csv file
"""


from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    api_link = "https://jsonplaceholder.typicode.com"
    r = get(f"{api_link}/users/{user_id}")
    name = r.json().get("name")
    r = get(f"{api_link}/todos/?userId={user_id}")
    todos = r.json()
    filename = f"{user_id}.csv"

    with open(filename, "w") as csvfile:
        for todo in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, name, todo.get('completed'), todo.get('title')))
