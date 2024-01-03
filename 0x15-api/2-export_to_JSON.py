#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script to get employee TODO list progress using a REST API and export data in JSON format.

Usage:
    python script.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee.

Requirements:
    - urllib or requests module
    - pycodestyle (version 2.8.*)

Example:
    python script.py 1
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(base_url.format(user_id))

    name = user.json().get('username')
    todos = requests.get(todos_url)

    todos_users = {}
    tasks = []

    for task in todos.json():
        if task.get('userId') == int(user_id):
            task_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')
                    }
            tasks.append(task_dict)
        todos_users[user_id] = tasks

    file = user_id + '.json'

    with open(file, mode="w") as user_file:
        json.dump(todos_users, user_file)
