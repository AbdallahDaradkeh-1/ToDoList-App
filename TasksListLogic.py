from datetime import date
import shelve, traceback
import LoadData, HelperMethods
from Task import Task
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
        HelperMethods.deleteGeneralList(self.tasks_lists)
      elif deleteOption == 2:
        self.print_tasks_list_info()
        print("Enter TasksList Title You Wanna Delete")
        inputTitle = input()
        deleteSpecificTaskList(inputTitle, self.tasks_lists)
      elif deleteOption == 3:
        print("Cancel...")
      else:
        print("Invalid Input")

    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)



def deleteSpecificTaskList(title, list):
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
  
def FindSpecificTaskList(self, list):
   index = 1
   outputs = 0
   self.print_tasks_list_info()
   print("Enter TasksList Name You are Searching For:")
   try:
    tasksListTitle = input()
   except Exception as error:
         error_info = traceback.extract_tb(error.__traceback__)[-1]
         print("Error Type:", type(error).__name__)
         print("Error Message:", error)
         print("Line Number:", error_info.lineno)
   for CurrenttasksList in list:
      if tasksListTitle.lower() in CurrenttasksList.name.lower():
         print(index, CurrenttasksList.name, CurrenttasksList.date)
         outputs += 1
         index += 1

   if outputs == 0:
    print("No TasksList With Such Name", tasksListTitle)

    
def add_task(self):
    try:
      self.load_tasks_list_data()
      self.print_tasks_list_info()
      print("Choose TasksList Name You want to add a Task To:")
      tasksListName = input()
      isTasksListNameExist = False
      index = 0
      for tasksList in self.tasks_lists:
        if tasksListName.lower() == tasksList.name.lower():
          isTasksListNameExist = True
          break
        index += 1

      if isTasksListNameExist:
        tasksList = self.tasks_lists[index]
      else:
        print("No existing TasksList With Such Name:", tasksListName)
        return
      

      print("Enter Task Name:")
      taskName = input()

      task = Task(taskName)
      tasksList.tasks.append(task) 

      print(taskName, "Task Has Been Created And Added To the chosen TasksList")
      # I Should update the list, but first let us test it 
    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)   
    
