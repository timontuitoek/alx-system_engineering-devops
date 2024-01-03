#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script to get employee TODO list progress
using a REST API and export data in CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(base_url, user_id)
    todos_str = '{}todos?userId={}'.format(base_url, user_id)
    file = '{}.csv'.format(user_id)

    res = requests.get(user_str)
    username = res.json().get('username')

    res = requests.get(todos_str)
    tasks = []
    for task in res.json():
        tasks.append([user_id, username,
                      task.get('completed'), task.get('title')])

    with open(file, mode='w') as emp_file:
        emp_writer = csv.writer(emp_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            emp_writer.writerow(task)
