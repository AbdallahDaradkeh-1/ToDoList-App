from datetime import date
import traceback
import shelve


class ToDoListOperations:
  def __init__(self):
    self.tasks_list = []

  def load_data(self):
    with shelve.open("local_storage") as db:  
      loaded_tasks_list = db.get("tasks_list", [])
      self.tasks_list = loaded_tasks_list
      print("Data Has Been Loaded")
  
  def create_tasks_list(self):
    try:
      # Ask user To Enter Task Name
      print("Enter TasksList Name, please:")
      task_name = input()

      new_task = TasksList(task_name)

      self.tasks_list.append(new_task)
      with shelve.open("local_storage") as db:
        db["tasks_list"] = self.tasks_list
        print("TasksList Has Been Saved To A Local File 'local_storage'")

    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)

  def print_tasks_list_info(self):
    for task in self.tasks_list:
      print(task.name, task.date)



class TasksList:
  def __init__(self, name):
    self.name = name
    self.date = date.today()














# Quick Test

taskList1 = TasksList("Wednesday")

print(taskList1.name, taskList1.date)
