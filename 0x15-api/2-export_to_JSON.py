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

import requests
import sys
import json

def get_employee_todo_progress(employee_id):
    """
    Get employee TODO list progress and export data in JSON format.

    Args:
        employee_id (int): The ID of the employee.
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

    # Create JSON file
    json_file_name = f"{user_id}.json"
    json_data = {"USER_ID": []}

    # Prepare data for JSON
    for todo in todos_data:
        task_completed_status = "Completed" if todo.get("completed") else "Not Completed"
        task_title = todo.get("title")
        user_task_data = {"task": task_title, "completed": task_completed_status, "username": employee_name}
        json_data["USER_ID"].append(user_task_data)

    # Write JSON data to file
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"JSON file '{json_file_name}' created successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
