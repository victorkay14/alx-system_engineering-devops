i#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Extract completed tasks
        completed_tasks = [task for task in todos_data if task.get('completed')]

        # Display progress information
        print(f"Employee {user_data['name']} is done with tasks "
              f"({len(completed_tasks)}/{len(todos_data)}):")

        for task in completed_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
