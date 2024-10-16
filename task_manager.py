class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

import json
import os

# Dummy login function
def login():
    print("Welcome to Task Manager! Please log in.")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Dummy credentials
    if email == "testuser@example.com" and password == "password123":
        print("Login successful!")
        return True
    else:
        print("Login failed! Please try again.")
        return False


# Load tasks from a file (tasks.json)
def load_tasks(file_name='tasks.json'):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return [Task(**task) for task in json.load(file)]
    return []

# Save tasks to a file (tasks.json)
def save_tasks(tasks, file_name='tasks.json'):
    with open(file_name, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)


# Add a new task
def add_task(tasks, title):
    new_id = len(tasks) + 1
    task = Task(new_id, title)
    tasks.append(task)
    save_tasks(tasks)

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        print(f"ID: {task.id} | Title: {task.title} | Status: {status}")

# Delete a task by its ID
def delete_task(tasks, task_id):
    tasks = [task for task in tasks if task.id != task_id]
    save_tasks(tasks)
    return tasks

# Mark a task as complete
def mark_task_complete(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            break
    save_tasks(tasks)

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the task title: ")
            add_task(tasks, title)
            print(f"Task '{title}' added.")

        elif choice == '2':
            view_tasks(tasks)

        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            tasks = delete_task(tasks, task_id)
            print(f"Task {task_id} deleted.")

        elif choice == '4':
            task_id = int(input("Enter the task ID to mark as complete: "))
            mark_task_complete(tasks, task_id)
            print(f"Task {task_id} marked as complete.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if login():
        main()
    else:
        print("Exiting application...")
          

if __name__ == "__main__":
    main()


