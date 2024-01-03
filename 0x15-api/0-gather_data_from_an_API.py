#!/usr/bin/python3
"""
Script to get employee TODO list progress using a REST API.
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Get employee TODO list progress and display on standard output.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get("completed"))

    # Display progress information
    print(f"Employee {employee_name} is done with tasks /"
          f"({completed_tasks}/{total_tasks}): ")
    print(f"{employee_name}: {completed_tasks}/{total_tasks}")

    # Display completed tasks titles
    for todo in todos_data:
        if todo.get("completed"):
            print(f"\t{todo['title']}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
