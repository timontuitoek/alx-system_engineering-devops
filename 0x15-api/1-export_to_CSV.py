#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script to get employee TODO list progress
using a REST API and export data in CSV format.
"""

import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """
    Get employee TODO list progress and export data in CSV format.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data.get("id")
    employee_name = user_data.get("name")

    # Fetch todos for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = [
            'USER_ID',
            'USERNAME',
            'TASK_COMPLETED_STATUS',
            'TASK_TITLE'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Write each task to CSV
        for todo in todos_data:
            task_completed_status = "Completed" \
                if todo.get("completed") else "Not Completed"
            task_title = todo.get("title")
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task_completed_status,
                'TASK_TITLE': task_title
            })

    print(f"CSV file '{csv_file_name}' created successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
