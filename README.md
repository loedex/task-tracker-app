# Task Tracker Mini Project

A menu-based Python Task Tracker application built for PSEB DEPLOY AI Engineering Bootcamp (Week 1, Day 2). It allows users to manage daily tasks with persistent storage using JSON.

## Features
- **Add Task**: Add a new task title (stored as Pending). Validates against empty titles.
- **View Tasks**: Display a numbered list of all tasks with their current status (`[Pending]` or `[Done]`).
- **Complete Task**: Mark any existing task as completed (`[Done]`).
- **Delete Task**: Remove a task from the list by its number.
- **Persistence**: Automatically saves and loads tasks from a `tasks.json` file.
- **Error Handling**: Handles invalid menu choices, out-of-range task numbers, non-numeric inputs, and missing JSON files.

## How to Run
1. Ensure Python 3 is installed.
2. Run the script in your terminal or Google Colab runtime:
   ```bash
   python mini_task_tracker.py