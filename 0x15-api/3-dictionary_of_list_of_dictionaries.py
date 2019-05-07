#!/usr/bin/python3
"""exports python script to export data in the JSON format"""
from sys import argv
import json
import requests
if __name__ == "__main__":

    url = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = url.json()

    usrs = requests.get('https://jsonplaceholder.typicode.com/users')
    usrs = usrs.json()

    json_file = "todo_all_employees.json"

    data = {}
    todo_task_list = []
    for user in usrs:
        USERNAME = user.get('username')
        USER_ID = user.get('id')
        for task in todo_list:
            if task['userId'] is USER_ID:
                task_dict = {}
                task_dict["task"] = task.get('title')
                task_dict["completed"] = task.get('completed')
                task_dict["username"] = USERNAME
                todo_task_list.append(task_dict)
            data[USER_ID] = todo_task_list
    with open(json_file, 'w') as j:
        json.dump(data, j)
