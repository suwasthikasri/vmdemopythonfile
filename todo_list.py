"""
Simple To-Do List App
Author: Suwasthika Sri
Description: A command-line To-Do List to add, view, and remove tasks.
"""

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def view_tasks(tasks):
    print("\n📋 Your To-Do List:")
    if not tasks:
        print("  (No tasks yet! Add one.)")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "⬜"
            print(f"  {i}. {status} {task['title']}")
    print()


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"  ✔ Task '{title}' added!\n")
    else:
        print("  ⚠ Task cannot be empty.\n")


def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"  ✅ Task '{tasks[num - 1]['title']}' marked as done!\n")
        else:
            print("  ⚠ Invalid number.\n")
    except ValueError:
        print("  ⚠ Please enter a valid number.\n")


def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  🗑 Task '{removed['title']}' removed!\n")
        else:
            print("  ⚠ Invalid number.\n")
    except ValueError:
        print("  ⚠ Please enter a valid number.\n")


def main():
    print("=" * 40)
    print("       📝 Simple To-Do List App")
    print("=" * 40)

    tasks = load_tasks()

    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("  ⚠ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
