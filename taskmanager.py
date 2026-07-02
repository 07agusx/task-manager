import json

task_list = []
cont_ids = 0 

def json_task(task_list, cont_ids):
    json_file = "task_manager.json"
    with open(json_file, "w") as task_data:
        data = {"tasks": task_list, "ids": cont_ids}
        json.dump(data, task_data)

def json_verify():
    try:
        with open("task_manager.json", "r") as stored_tasks:
            data = json.load(stored_tasks)
            return data["tasks"], data["ids"]
    except FileNotFoundError:
        return [], 0

def add_task(task_list, task):
    global cont_ids
    if len(task.strip()) <= 0 or task.isdigit():
        print("Please enter a valid task.")
    else:
        task_list.append({"id": cont_ids, "name": task, "complete": False})
        cont_ids +=1 
        print(f"New task added: ID = {task_list[-1]['id']} | Name = {task_list[-1]['name']} | Complete = {task_list[-1]['complete']}")
        json_task(task_list, cont_ids)

def complete_task(task_list, ids):
    global cont_ids
    for tasks in task_list: 
        if ids == tasks["id"]:
            if  tasks["complete"]:
                print("The task has already been completed.")
                break
            else:
                tasks["complete"] = True
                print(f"The following task was completed: {tasks}")
                json_task(task_list, cont_ids)
                break
    else:
        print("Enter a valid ID. If you do not know the IDs, use option 4.")

def delete_task(task_list, ids):
    global cont_ids
    for tasks in task_list: 
        if ids == tasks["id"]: 
                print(f"The following task was deleted: {tasks}")
                task_list.remove(tasks) 
                json_task(task_list, cont_ids)
                break
    else:
        print("Enter a valid ID. If you do not know the IDs, use option 4.")

def show_task(task_list):
    for tasks in task_list:
        print(f"ID = {tasks["id"]} | Name = {tasks["name"]} | Complete = {tasks["complete"]}")

task_list, cont_ids = json_verify()

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
            add = input("Enter the name of the task you wish to add: ")
            add_task(task_list, add)
        case "2":
            try:
                update = int(input("Enter the ID of the task you wish to update: "))
            except ValueError:
                print("Enter a valid ID.")
            else:
                complete_task(task_list, update)
        case "3":
            try:
                delete = int(input("Enter the ID of the task you wish to delete: "))
            except ValueError:
                print("Enter a valid ID.")
            else:
                delete_task(task_list, delete)
        case "4":
            if len(task_list) > 0:
                print("--Task list--")
                show_task(task_list)
            else:
                print("The list is empty; add tasks to view them.")
        case "5":
            print("Exiting the task manager...")
            break
        case _:
            print("ERROR: Please enter a valid option.")