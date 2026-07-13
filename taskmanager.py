import json

def json_verify():
    try:
        with open("task-manager.json") as stored_task:
            data = json.load(stored_task)
            return data["tasks"], data["ids"]
    except FileNotFoundError:
        return [], 0

class Task:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.complete = False

    def __str__(self):
        return f"Name: {self.name} | ID: {self.id} | Complete: {self.complete}"

class TaskManager:
    def __init__(self):
        self.stored_task, self.cont_id = json_verify() 
        self.task_list = []
        self.convert_obj(self.stored_task)

    def convert_obj(self, stored_task):
        for tasks in stored_task:
            task = Task(tasks["name"])
            task.id = tasks["id"]
            task.complete = tasks["complete"]
            self.task_list.append(task)

    def add_task(self, new_task):
        if isinstance(new_task, Task):
            if len(new_task.name.strip()) <= 0 or new_task.name.isdigit():
                print("The task entered is invalid.")
            else:
                self.task_list.append(new_task)
                self.cont_id += 1
                new_task.id = self.cont_id
                print(f"- New task added => {new_task}")
                self.json_task()
        else:
            print("The task entered is invalid.")

    def del_task(self, del_task):
        for task in self.task_list:
            if del_task == task.id:
                self.task_list.remove(task)
                print(f"- Task removed => {task}")
                self.json_task()
                break
        else:
            print("The ID of the task entered is invalid.")

    def complete_task(self, complete_task):
        for task in self.task_list:
            if complete_task == task.id:
                if task.complete:
                    print("The entered task has already been completed.")
                    break
                else:
                    task.complete = True
                    print(f"- Task completed => {task}")
                    self.json_task()
                    break
        else:
            print("The ID of the task entered is invalid.")

    def show_tasks(self):
        if len(self.task_list) > 0:
            for tasks in self.task_list:
                print(f"- Task-Manager - {tasks}")
        else:
            print("The Task Manager is empty.")

    def convert_dict(self):
        task_dict = []
        for task in self.task_list:
            task_dict.append({"id": task.id, "name": task.name, "complete": task.complete})
        return task_dict
    
    def json_task(self):
        json_file = "task-manager.json"
        with open(json_file, "w") as task_data:
            data = {"tasks": self.convert_dict(), "ids": self.cont_id}
            json.dump(data, task_data, indent=4)

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
            task_manager.add_task(task)
        case "2":
            try:
                update = int(input("Enter the ID of the task you wish to update: "))
            except ValueError:
                print("Enter a valid ID.")
            else:
                task_manager.complete_task(update)
        case "3":
            try:
                delete = int(input("Enter the ID of the task you wish to delete: "))
            except ValueError:
                print("Enter a valid ID.")
            else:
                task_manager.del_task(delete)
        case "4":
                task_manager.show_tasks()
        case "5":
            print("Exiting the task manager...")
            break
        case _:
            print("ERROR: Please enter a valid option.")