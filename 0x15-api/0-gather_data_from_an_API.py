#!/usr/bin/python3
"""using REST API that returns status of a todo list"""
import requests
from sys import argv


if __name__ == "__main__":

    passed_id = argv[1]
    url = requests.get('https://jsonplaceholder.typicode.com/todos',
                       params={'userId': passed_id})
    todo_list = url.json()
    TOTAL_NUMBER_OF_TASKS = len(todo_list)

    usr = requests.get('https://jsonplaceholder.typicode.com/users',
                       params={'id': passed_id})
    usr = usr.json()
    EMPLOYEE_NAME = usr[0].get('name')

    list_of_completed = []
    NUMBER_OF_DONE_TASKS = 0
    for task in todo_list:
        if task.get('completed') is True:
            list_of_completed.append(task)
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in list_of_completed:
        print("\t "+task.get('title'))
