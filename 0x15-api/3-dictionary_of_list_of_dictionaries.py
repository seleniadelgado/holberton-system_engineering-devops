#!/usr/bin/python3
"""exports python script to export data in the JSON format]"""
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
    data_list = []
    for user in usrs:
        USERNAME = user.get('username')
        USER_ID = user.get('id')
        for task in todo_list:
            little_dict = {}
            little_dict["task"] = task.get('title')
            little_dict["completed"] = task.get('completed')
            little_dict["username"] = USERNAME
            data_list.append(little_dict)
        data[USER_ID] = data_list
    with open(json_file, 'w') as j:
        json.dump(data, j)
