print("Enter you tasks to do\n")

tasks = []

def options():
    print("""
    1. Add Task
    2. Remove Task
    3. Save and Exit
    4. Show tasks
    """)

def add_task():
    task = input("Enter task to add:- ")
    tasks.append(task)
    print()

def remove_task(index):
    index -= 1
    if index >= 0 and index < len(tasks):
        tasks.pop(index)
    else:
        print("Task number does not exist\n")
        return
    
    print("Task removed.\n")

def show_tasks():
    if not tasks:
        print("No tasks available")
        return
    for i , task in enumerate(tasks):
        print(f"{i+1}. {task}")
    
try:
    with open("tasks.txt" , "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    print("No saved tasks found.\n")

while True:
    options()
    try:
        option = int(input("Enter your option:- "))
    except ValueError:
        print("Invalid input")
        continue
    
    if option == 1:
        add_task()
    elif option == 2:
        try:
            index = int(input("Enter task number to remove:- "))
            remove_task(index)
        except ValueError:
            print("Invalid task number\n")
            continue
    elif option == 3:
        print("Saved and exited.\n")
        with open("tasks.txt" , "w") as file:
            for task in tasks:
                file.write(task +"\n")
        break
    elif option == 4:
        show_tasks()
    else:
        print("Invalid option")






