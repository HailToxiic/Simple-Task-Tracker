# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress
import json
from datetime import datetime

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def addTask():

    description = input("Enter task description: ").strip()
    current_time = datetime.now().isoformat()

    if not description:
        print("Task description is required")
        return

    if not tasks:
        new_id = 1

    else:
        new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "description": description,
        "status": False,
        "createdAt": current_time,
        "updatedAt": current_time,
    }

    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def delTask():

    try:
        task_id = int(input("Enter task # to delete: "))
    except ValueError:
        print("Invalid input")
        return

    for task in tasks:
        if task["id"] == int(task_id):
            tasks.remove(task)
            print("Task deleted")
            break

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def updateTask():

    for task in tasks:
        print(f"Task #: {task['id']}")
        print(f"Description: {task['description']}")
        print("-"*20)

    task_id = input("Enter task # to update: ")
    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = True
            task['updatedAt'] = datetime.now().isoformat()
            print("Task updated")
            break

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def listTask():

    for task in tasks:

        status_tasks = "Complete" if task['status'] else "Pending"
        print(f"Task #: {task["id"]}")
        print(f"Description: {task['description']}")
        print(f"Status of Task: {status_tasks}")
        print("-"*20)

    if not tasks:
        print("No tasks found")

def main():

    print("Task Tracker")
    print("1. Add new task")
    print("2. Delete task")
    print("3. Update task")
    print("4. List tasks")
    print("5. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()

        elif choice == "2":
            delTask()

        elif choice == "3":
            updateTask()

        elif choice == "4":
            listTask()

        elif choice == "5":
            break


main()

