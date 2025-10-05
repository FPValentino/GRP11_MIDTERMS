# currently implemented standards:
# 1. Docstring for functions
# 2. Indentation of code blocks
# 3. Implementing naming convention (snake_case for functions and variables)

# toDoApp.py

tasks=[]

def add_task(task) :
    """Add a new task to the tas list.""

    Args:
        task (str): The task to be added.
    """
    tasks.append(task)
    print("task added!")

def show_tasks():
    """Shows all tasks in the task list.
    """
    if len(tasks)==0 :
        print("no tasks yet")
    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])

def remove_task(tasknumber):
    """Removes task from the task list.

    Args:
        tasknumber (int): The index of the task to be removed (1-based index).
    """
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
    """The main function to run the to-do app.
    """
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            add_task(t)
        elif ch=="2":
            show_tasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            remove_task(n)   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
main()
