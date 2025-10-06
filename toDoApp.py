# toDoApp.py
"""A simple to-do list application that allows users to add, view, and remove tasks."""
import os

TASKS_FILE = "tasks.txt"


def clear_screen():
    """Clear the terminal screen for better UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')


def load_tasks():
    """Load tasks from file if it exists.

    Returns:
        list: A list of tasks loaded from the file, or an empty list if file doesn't exist.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []


def save_tasks(tasks):
    """Save tasks to file.

    Args:
        tasks (list): The list of tasks to save to the file.
    """
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(tasks, task):
    """Add a new task to the task list.

    Args:
        tasks (list): The current list of tasks.
        task (str): The task to be added.

    Returns:
        list: The updated list of tasks with the new task added.
    """
    tasks.append(task)
    save_tasks(tasks)
    print("\nTask added successfully!")
    input("\nPress Enter to continue...")
    return tasks


def show_tasks(tasks, pause=True):
    """Shows all tasks in the task list.

    Args:
        tasks (list): The list of tasks to display.
        pause (bool): Whether to wait for user input before continuing. Default is True.
    """
    print("\n" + "="*50)
    print("YOUR TASKS".center(50))
    print("="*50)
    
    if len(tasks) == 0:
        print("\n  No tasks yet. Add one to get started!")
    else:
        print()
        for i, task in enumerate(tasks, start=1):
            print(f"  [{i}] {task}")
    
    print("="*50)
    if pause:
        input("\nPress Enter to continue...")


def remove_task(tasks, tasknumber):
    """Removes task from the task list.

    Args:
        tasks (list): The current list of tasks.
        tasknumber (int): The index of the task to be removed (1-based index).

    Returns:
        list: The updated list of tasks with the specified task removed.
    """
    if 0 <= tasknumber < len(tasks):
        removed_task = tasks.pop(tasknumber)
        save_tasks(tasks)
        print(f"\nTask '{removed_task}' removed successfully!")
    else:
        print("\nInvalid task number!")
    input("\nPress Enter to continue...")
    return tasks


def main():
    """The main function to run the to-do app."""
    tasks = load_tasks()
    while True:
        clear_screen()
        print("\n" + "="*50)
        print("TO-DO LIST APPLICATION".center(50))
        print("="*50)
        print("\n  [1] Add Task")
        print("  [2] Show Tasks")
        print("  [3] Remove Task")
        print("  [4] Exit")
        print("\n" + "="*50)
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            clear_screen()
            print("\n" + "="*50)
            print("ADD NEW TASK".center(50))
            print("="*50)
            task_input = input("\nEnter task: ")
            if task_input.strip():
                tasks = add_task(tasks, task_input)
            else:
                print("\nTask cannot be empty!")
                input("\nPress Enter to continue...")
                
        elif choice == "2":
            clear_screen()
            show_tasks(tasks)
            
        elif choice == "3":
            clear_screen()
            show_tasks(tasks, pause=False)
            if len(tasks) > 0:
                try:
                    task_num = int(input("\nEnter task number to remove: "))
                    tasks = remove_task(tasks, task_num - 1)
                except ValueError:
                    print("\nPlease enter a valid number!")
                    input("\nPress Enter to continue...")
            else:
                input("\nPress Enter to continue...")
                
        elif choice == "4":
            clear_screen()
            print("\n" + "="*50)
            print("Thank you for using To-Do List App!".center(50))
            print("="*50)
            print("Que, Adrian".center(50))
            print("Que, Desmond".center(50))
            print("Valentino, Ferdinand".center(50))
            print()
            break
            
        else:
            print("\nInvalid choice! Please enter 1-4.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()