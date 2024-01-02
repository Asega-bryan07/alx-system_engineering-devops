#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python
script to export data in the CSV format.
Requirements:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME",
"TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
'''
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

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeId, username, task.get('completed'), task
                .get('title')))
