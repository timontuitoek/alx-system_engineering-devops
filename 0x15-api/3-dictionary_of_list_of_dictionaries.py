#!/usr/bin/python3
"""
Script to get employee TODO list
progress using a REST API and export data in JSON format.
"""
import json
import requests
import sys


def export_todo_to_json():
    """
    Export TODO list data for all employees in JSON format.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = '{}users'.format(base_url)

    # Fetch user information
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Create a dictionary to store data
    all_employees_data = {}

    for user in users_data:
        user_id = user.get('id')
        user_name = user.get('name')

        todos_url = '{}todos?userId={}'.format(base_url, user_id)

        # Fetch TODO list for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Collect tasks data for the user
        user_tasks_data = []
        for task in todos_data:
            task_data = {
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks_data.append(task_data)

        # Add user tasks data to the dictionary
        all_employees_data[user_id] = user_tasks_data

    # Write the data to JSON file
    json_file_name = 'todo_all_employees.json'
    with open(json_file_name, 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)

    print(f"JSON file '{json_file_name}' created successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python script.py")
        sys.exit(1)

    export_todo_to_json()
