from datetime import date
import shelve, traceback
import loadData
import TasksList

def create_tasks_list(self):
    try:
      # Ask user To Enter Task Name
      print("Enter TasksList Name, please:")
      task_name = input()

      new_task = TasksList.TasksListc(task_name)

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
    print("Existing TasksLists:")
    i = 1
    for task in self.tasks_lists:
      print(i, task.name, task.date)
      i+=1
def deleteListsOptions(self):
    try:  
      print("Delete Options")
      print("Choose What do you want to delete?")
      print("1. Delete Tasks Lists")
      print("2. Delete Specific Tasks List")
      print("3. Cancel")
      deleteOption = int(input())
      if deleteOption == 1:
        self.deleteGeneralList(self.tasks_lists)
      elif deleteOption == 2:
        self.print_tasks_list_info()
        print("Enter TasksList Title You Wanna Delete")
        inputTitle = input()
        self.deleteSpecificTaskList(inputTitle, self.tasks_lists)
      elif deleteOption == 3:
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

def deleteSpecificTaskList(self, title, list):
   # Start save the index
  index = 0
   # Return List is Empty message if it is empty
  if len(list) == 0:
      print("List Is Empty, no TasksList To Delete")
      return
   # Go Through All List Items
  for item in list:
   # If title is there, pop that item, Continuesly increase the index to pop at it
    if item.name.lower() == title.lower():
       list.pop(index)
       with shelve.open('local_storage') as db:
          db["tasks_lists"] = list
          print(title, "TasksList Has Been Deleted From The List")
       return
    index += 1
  

  print("TasksList with such title is not exist")
  
   

  

def load_tasks_list_data(self):
    loadData.load_tasks_list_data(self)       

