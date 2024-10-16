import json

class Task():
    def __init__(self, task_id,title,description,due_date,status='Pending'):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

    def taskedit(self, title,description,due_date,status):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

    def saveas_dic(self):
        self.taskdict = {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
            }
        return self.taskdict
    
    def displayas_js(self,tsk):
        self.tsk = {
            self.task_id : tsk['task_id'],
            self.title : tsk['title'],
            self.description : tsk['description'],
            self.due_date : tsk['due_date'],
            self.status : tsk['status']
            }

    
class TaskManager():
    def __init__(self,filename="task.json"):
        self.filename = filename
        self.tasks = []
        self.loadtasks()

    def addtask(self):
        task_id = len(self.tasks) + 1
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date: ")
        status = input("Enter task status: ")
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task.saveas_dic())

    def listtask(self, status=None):
        if status is None:
            print("All Tasks")
            for task in self.tasks:
                print(task['task_id'],task['title'],task['description'],task['due_date'],task['status'])
        else:
            print("Tasks with status: ", status)
            found=False
            for task in self.tasks:
                if task['status'] == status:
                    found=True
                    print(task['task_id'],task['title'],task['description'],task['due_date'],task['status'])
            if not found:
                print("No tasks with status: ", status)

    def updatetask(self):
        self.listtask()
        task_id = int(input("Enter task id to update: "))
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['title'] = input("Enter new title: ")
                task['description'] = input("Enter new description: ")
                task['due_date'] = input("Enter new due date: ")
                task['status'] = input("Enter new status: ")
                break

    def deletetask(self):
        self.listtask()
        task_id = int(input("Enter task id to delete: "))
        for task in self.tasks:
            if task['task_id'] == task_id:
                self.tasks.remove(task)
                break

    def savetasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def loadtasks(self):
        try:
            with open(self.filename, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task.displayas_js(tsk) for tsk in task_data]
        except FileNotFoundError:
            print("No existing tasks found. Starting with an empty list.")

    def taskrun(self):
        while True:
            print("\n1. Add Task")
            print("2. List Tasks")
            print("3. List Task by status")
            print("4. Update Task")
            print("5. Delete Tasks")
            print("6. Save & Exit Tasks")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addtask()
            elif choice == "2":
                self.listtask()
            elif choice == "3":
                status=input("Enter status to filter by (Pending, In Progress, Completed):")
                self.listtask(status)
            elif choice == "4":
                self.updatetask()
            elif choice == "5":
                self.deletetask()
            elif choice == "6":
                self.savetasks()
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

x=TaskManager()
x.taskrun()




        

    
    
