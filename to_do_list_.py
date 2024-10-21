# -*- coding: utf-8 -*-
"""2 to do list .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/118t8fEyxqzgugPRjx6UqIpx_ewqnX3ht
"""

import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task, status = line.strip().split(' | ')
                tasks.append({'task': task, 'status': status})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['status']}\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task['status'] == 'done' else "✗"
            print(f"{idx}. {task['task']} - {status}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({'task': task, 'status': 'not done'})
    save_tasks(tasks)
    print(f"\nTask '{task}' added successfully.")

def mark_task_done(tasks):
    display_tasks(tasks)
    if tasks:
        task_number = int(input("\nEnter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['status'] = 'done'
            save_tasks(tasks)
            print(f"\nTask '{tasks[task_number - 1]['task']}' marked as done.")
        else:
            print("Invalid task number!")

def delete_task(tasks):
    display_tasks(tasks)
    if tasks:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"\nTask '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number!")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()