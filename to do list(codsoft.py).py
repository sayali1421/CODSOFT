import json
import os


FILENAME = "tasks.json"


# Function to load existing tasks

def load_tasks():
    # If the file exists, open it and read the tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    # If not, just start with an empty list
    return []


# Function to save tasks to a file

def save_tasks(tasks):
    # Write (save) all tasks into the JSON file
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


# Function to show all tasks

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found yet.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        # Show [x] if done, [ ] if not done
        mark = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {mark} {task['title']}")


# Function to add a new task

def add_task(tasks):
    title = input("\nEnter a new task: ").strip()
    if not title:
        print("Task name cannot be empty.")
        return
    
    # Create a dictionary for the new task
    new_task = {"title": title, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


# Function to mark a task as done

def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("\nEnter the number of the task to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Function to delete a task

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main program (menu)

def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye! All your tasks are saved.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
