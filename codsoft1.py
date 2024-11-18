import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load existing tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task['completed'] else "❌"
            print(f"{i}. [{status}] {task['title']}: {task['description']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Update an existing task
def update_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['title'] = input("Enter new task title: ")
            tasks[task_index]['description'] = input("Enter new task description: ")
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

