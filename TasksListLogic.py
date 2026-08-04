from datetime import date
import shelve, traceback

def create_tasks_list(self):
    try:
      # Ask user To Enter Task Name
      print("Enter TasksList Name, please:")
      task_name = input()

      new_task = TasksList(task_name)

      self.tasks_lists.append(new_task)
      with shelve.open("local_storage") as db:
        db["tasks_lists"] = self.tasks_lists
        print("TasksList Has Been Saved To A Local File 'local_storage'")

    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)

def print_tasks_list_info(self):
    for task in self.tasks_lists:
      print(task.name, task.date)
def deleteListsOptions(self):
    try:  
      print("Delete Options")
      print("Choose What do you want to delete?")
      print("1. Delete Tasks Lists")
      print("2. Cancel")
      deleteOption = int(input())
      if deleteOption == 1:
        self.deleteGeneralList(self.tasks_lists)
      elif deleteOption == 2:
        print("Cancel...")
      else:
        print("Invalid Input")

    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)

def deleteGeneralList(self, list):
      i = 0
      if len(list) == 0:
        print("This List Is Empty")

      list.clear()
        
      with shelve.open("local_storage") as db:
          db["tasks_lists"] = list
          print("This List Updates Have Been Saved")

def load_data(self):
    with shelve.open("local_storage") as db:  
      loaded_tasks_lists = db.get("tasks_lists", [])
      self.tasks_lists = loaded_tasks_lists
      print("Data Has Been Loaded")        

class TasksList:
  def __init__(self, name):
    self.name = name
    self.date = date.today()

