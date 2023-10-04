#!/usr/bin/python3
"""Exports data in CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
	tmp = requests.get("https://jsonplaceholder.typicode.com/users/{:}".format(argv[1])).json()
	temp = requests.get("https://jsonplaceholder.typicode.com/todos/?userId={:}".format(argv[1])).json()
	user_id = argv[1]
	user_name = tmp.get("username")
	with open("{:}.csv".format(argv[1]), mode="w") as file:
		user_id_w = csv.writer(file, quoting=csv.QUOTE_ALL)
		for e in temp:
			user_id_w.writerow([user_id, user_name, e.get("completed"), e.get("title")])
