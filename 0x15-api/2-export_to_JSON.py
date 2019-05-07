#!/usr/bin/python3
"""exports python script to export data in the JSON format]"""
from sys import argv
import json
import requests
if __name__ == "__main__":

    USER_ID = argv[1]
    url = requests.get('https://jsonplaceholder.typicode.com/todos',
                       params={'userId': USER_ID})
    todo_list = url.json()

    usr = requests.get('https://jsonplaceholder.typicode.com/users',
                       params={'id': USER_ID})
    usr = usr.json()
    USERNAME = usr[0].get('username')

    json_file = "{}.json".format(USER_ID)

    data = {}
    data_list = []

    for task in todo_list:
        little_dict = {}
        little_dict["task"] = task.get('title')
        little_dict["completed"] = task.get('completed')
        little_dict["username"] = USERNAME
        data_list.append(little_dict)
    data[USER_ID] = data_list
    with open(json_file, 'w') as j:
        json.dump(data, j)
