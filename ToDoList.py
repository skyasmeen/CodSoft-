tasks=[]
def add():
    task=input("enter a task:")
    tasks.append(task)
    print(f"task '{task}' added to list.")


def list():
    if not tasks:
        print("no tasks")
    else:
        for index, task in enumerate(tasks):
            print(f"Task #{index}.{task}")   
    
def delete():
    list()
    taskToDelete=int(input("enter the task to be deleted:"))
    if taskToDelete>=0 and taskToDelete<len(tasks):
        tasks.pop(taskToDelete)
        print(f"task '{taskToDelete}' removed from list.")
    else:
         print("Invalid input")
         

if  __name__=="__main__":
    while True:
        print("1.Add a task")
        print("2.delete a task")
        print("3.list all tasks:")
        print("4.Exit")

        choice=input("enter your choice:")

        if choice=='1':
            add()

        elif choice=='2':
             delete()
        elif choice=='3':
             list()
        elif choice=='4':
             break
        else:
            print("Invalid input")
            
