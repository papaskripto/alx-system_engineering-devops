#!/usr/bin/python3
""" Returns information about employee TODO list progress."""

import requests
from sys import argv


if __name__ == "__main__":
	user_id = argv[1]
	user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
		format(user_id), verify=False).json()
	todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
		format(user_id), verify=False).json()
	number_of_done_tasks = []
	for task in todo:
		if task.get("completed") is True:
			number_of_done_tasks.append(task.get("title"))
	print("Employee {} is done with tasks ({}/{}):".
		format(user.get("name"), len(number_of_done_tasks), len(todo)))
	for task in number_of_done_tasks:
		print("\t {}".format(task))
