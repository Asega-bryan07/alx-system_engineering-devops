#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
Requirements:
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    doUrl = url + "/todos"
    response = requests.get(doUrl)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username})

    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
