#!/usr/bin/python3
""" Returns information about employee TODO list progress."""

import requests
from sys import argv


if __name__ == "__main__":
	user_id = argv[1]
	user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
			format(user_id), verify=False).json()
	todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
			format(user_id), verify=False).json()
	completed = []
	for task in todos:
		if task.get("completed") is True:
			completed.append(task.get("title"))
	print("Employee {} is done with tasks ({}/{}):".
			format(user.get("name"), len(completed), len(todos)))
	for task in completed:
		print("\t {}".format(task))
