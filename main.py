from taskmanager import TaskManager
from task import Task

task_manager = TaskManager()

while True:
    print("")
    print("¡Welcome to the --Task Manager--!")
    print("""
            - - - Options - - -
          
1 = Add task
2 = Complete task
3 = Delete task
4 = Show task list and IDs
5 = Exit
          """)
    
    option = input("Enter an option: ")

    match option:
        case "1":
            new_task = input("Enter the name of the task you wish to add: ")
            task = Task(new_task)
            if task_manager.add_task(task):
                print(f"New task added => {new_task}")
            else:
                print("The task name entered is invalid.")
        case "2":
            try:
                update = int(input("Enter the ID of the task you wish to update: "))
            except ValueError:
                print("Enter a valid ID.")
            else:
                status,  task = task_manager.complete_task(update)

                match status:
                    case "already_completed":
                        print(f"The task -{task.name}- has already completed.")
                    case "completed":
                        print(f"Task completed => {task.name}")
                    case "not_found":
                        print("The ID entered is invalid.")
        case "3":
            try:
                delete = int(input("Enter the ID of the task you wish to delete: "))
            except ValueError:
                print("Enter a valid ID.")
            else:
                delete_task = task_manager.del_task(delete)
                if delete_task:
                    print(f"Task deleted => {delete_task} ")
                else:
                    print("The ID entered is invalid.")
        case "4":
                tasks = task_manager.show_tasks()
                if tasks:
                    for task in tasks:
                        print(f"- Task Manager => {task}")
                else:
                    print("The task manager is empty.")
        case "5":
            print("Exiting the task manager...")
            break
        case _:
            print("ERROR: Please enter a valid option.")