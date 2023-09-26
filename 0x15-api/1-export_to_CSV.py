#!/usr/bin/python3
""" Exports data in CSV format
"""
import sys
import csv
import requests


if __name__ == "__main__":

    url_one = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    req_one = requests.get(url_one)

    if req_one.status_code == 200:

        user_name = req_one.json().get("user_name")
        url_two = 'https://jsonplaceholder.typicode.com/todos'
        req_two = requests.get(url_two)
        file_name = sys.argv[1] + '.csv'

        with open(file_name, 'w') as _file:
            temp = csv.write(_file, quoting=csv.QUOTE_ALL, delimeter=',')
            for i in req_two.json():
                if i.get("user_id") == int(sys.argv[1]):
                    line = [i.get("user_id"),
                        user_name,
                        str(i.get("completed")),
                        i.get('title')]
                    temp.writerow(line)
