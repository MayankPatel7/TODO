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

def export():
    name = input("Enter a name for todo list: ")
    file = open("C:\\Users\\Mayank\\Downloads\\"+name+".txt" , "x")
    for i in range(len(tasks)):
        file.write(str(i+1)+". "+tasks[i]+"\n")
    print("Exported list as", name+".txt")
    file.close()

while start:
    option = int(input("""
1. Add task to list
2. Remove task from list
3. List all tasks
4. Export
5. Exit app
Choose an option: """))
    if option == 1:
        addTask()
    elif option == 2:
        removeTask()
    elif option == 3:
        displayTasks()
    elif option == 4:
        export()
    elif option == 5:
        print("**************** THANK YOU ****************")
        start = False
    else:
        print("ENTER A VALID OPTION")
