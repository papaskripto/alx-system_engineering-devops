#!/usr/bin/python3
""" Returns information about user TODO List progress
"""
import sys
import requests


if __name__ == "__main__":
    first_url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    first_request = requests.get(first_url)
    name = first_request.json().get("name")
    second_url = 'https://jsonplaceholder.typicode.com/todos'
    second_request = requests.get(second_url)
    task_names = []
    tasks = 0
    completed = 0
    for i in second_request.json():
        if i.get("user_id") == int(sys.argv[1]):
            tasks += 1
            if i.get("completed") is True:
                completed += 1
                task_names.append(i.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, completed, tasks))

    for i in task_names:
        print("\t {}".format(i))
