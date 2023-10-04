#!/usr/bin/python3
"""Python script.

This script returns information about employee TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
	number_of_done_tasks = 0
	total_number_of_tasks = 0
	completed_tasks = []
	tmp = requests.get('https://jsonplaceholder.typicode.com/users/{:}'.format(argv[1])).json()
	tmp_ = requests.get('https://jsonplaceholder.typicode.com/todos/?userId={:}'.format(argv[1])).json()
	for i in tmp_:
		total_number_of_tasks += 1
		if i.get('completed') is True:
			number_of_done_tasks += 1
			completed_tasks.append(i.get('title'))
	print("Employee {:} is done with tasks({:}/{:}):".format(tmp.get('name'), number_of_done_tasks, total_number_of_tasks))
	for j in completed_tasks:
		print("\t {:}".format(j))
