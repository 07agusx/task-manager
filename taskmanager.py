import json
from task import Task

def json_verify():
    try:
        with open("task-manager.json") as stored_task:
            data = json.load(stored_task)
            return data["tasks"], data["ids"]
    except FileNotFoundError:
        return [], 0

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
            if len(new_task.name.strip()) or new_task.name.isdigit():
                return False
            else:
                self.task_list.append(new_task)
                self.cont_id += 1
                new_task.id = self.cont_id
                self.json_task()
                return True
        else:
            return False

    def del_task(self, del_task):
        for task in self.task_list:
            if del_task == task.id:
                self.task_list.remove(task)
                self.json_task()
                return task
        else:
            return None

    def complete_task(self, complete_task):
        for task in self.task_list:
            if complete_task == task.id:
                if task.complete:
                    return "already_completed", task
                else:
                    task.complete = True
                    self.json_task()
                    return "completed", task
        else:
            return "not_found", None

    def show_tasks(self):
        if len(self.task_list) > 0:
            return self.task_list

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
