#!/usr/bin/python3
""" Returns information about employee TODO list progress."""

import requests
from sys import argv


if __name__ == "__main__":
	employee_id = argv[1]
	employee_name = requests.get("https://jsonplaceholder.typicode.com\
			/users/{}".format(employee_id), verify=False).json()
	total_number_of_tasks = requests.get("https://jsonplaceholder.typicode.com\
			/todos?userId={}".format(employee_id), verify=False).json()
	number_of_done_tasks = []
	for task in total_number_of_tasks:
		if task.get("completed") is True:
			number_of_done_tasks.append(task.get("title"))
	print("Employee {} is done with tasks ({}/{}):".format(employee_name.get\
			("name"), len(number_of_done_tasks), len(total_number_of_tasks)))
	for task in number_of_done_tasks:
		print("\t {}".format(task))
