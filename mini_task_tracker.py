# mini_task_tracker.py
# Student: Husnain Ahmad
# Roll no.: TRN-2026-002301
# Class: AI Engineering / Week 1, Day 2 - Task Tracker Mini Project

import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file at startup. Return empty list if file doesn't exist."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks.json was corrupted. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    """Save the current task list to tasks.json."""
    try:
        with open(FILENAME, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """Ask for a task title and store it as Pending."""
    title = input("Task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    """Show a numbered task list with Pending or Done."""
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\n--- TASK LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")

def complete_task(tasks):
    """Select a task number and mark its done field True."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Task number: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("Task completed.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid integer number.")

def delete_task(tasks):
    """Select a task number and remove that task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid integer number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Error: Invalid menu choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()