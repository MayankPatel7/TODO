print("**************** TODO ****************")
tasks = []
start = True

def addTask():
    task = input("Task: ")
    tasks.append(task)
    for i in range(len(tasks)):
        print(str(i+1)+". "+tasks[i])

def removeTask():
    for i in range(len(tasks)):
        print(str(i+1)+". "+tasks[i])
    option = int(input("Select a task to remove: "))
    tasks.remove(tasks[option-1])
    for i in range(len(tasks)):
        print(str(i+1)+". "+tasks[i])
    
def displayTasks():
    if len(tasks) > 0:
        for i in range(len(tasks)):
            print(str(i+1)+". "+tasks[i])
    else:
        print("The list is currently empty")

while start:
    option = int(input("""
1. Add task to list
2. Remove task from list
3. List all tasks
4. Exit app
Choose an option: """))
    if option == 1:
        addTask()
    elif option == 2:
        removeTask()
    elif option == 3:
        displayTasks()
    elif option == 4:
        start = False
    else:
        print("ENTER A VALID OPTION")