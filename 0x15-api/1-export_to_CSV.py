#!/usr/bin/python3
"""using REST API that returns status of a to do list"""
from sys import argv
import csv
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

    for task in todo_list:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')

    csv_file = "{}.csv".format(USER_ID)
    # where to add the file that is downloaded.

    with open(csv_file, "w") as f:
        # 'w' to write string to a file.
        f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo_list:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            f.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
