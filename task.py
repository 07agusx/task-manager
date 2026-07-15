class Task:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.complete = False

    def __str__(self):
        return f"Name: {self.name} | ID: {self.id} | Complete: {self.complete}"