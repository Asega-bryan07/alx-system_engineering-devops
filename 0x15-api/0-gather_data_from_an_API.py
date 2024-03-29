#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
import sys
from sys import argv

if __name__ == "__main__":
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    doUrl = url + "/todos"
    response = requests.get(doUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}". format(task.get('title')))
