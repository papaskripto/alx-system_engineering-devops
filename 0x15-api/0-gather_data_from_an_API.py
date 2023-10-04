#!/usr/bin/python3
"""Python script.
This script returns information about user todo list progress.
"""
import requests


def get_employee_progress(emp_id):
    """Function
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    emp_url = api_url + "/users/" + str(emp_id)
    todos_url = api_url + "/todos?user_id=" + str(emp_id)

    try:
        # Fetch employee info
        emp_res = requests.get(emp_url)
        emp_data = emp_res.json()
        employee_name = emp_data["name"]

        # Fetch employee todo list
        todos_res = request.get(todos_url)
        todos_data = todos_res.json()

        # Determine progress
        total_number_of_tasks = len(todos_data)
        number_of_done_tasks = sum(1 for todo in todos_data if todo['completed'])

        message = "Employee {} is done with tasks ({}/{})".format(
               employee_name, number_of_done_tasks, total_number_of_tasks)
        print(message)
        for todo in todos_data:
            if todo['completed']:
                print ("\t{}".format(todo['title']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    emp_id = int(input("Enter Employee ID: "))
    get_employee_progress(emp_id)
