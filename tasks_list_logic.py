from datetime import date
import shelve, traceback
import load_data, helper_methods
from task import Task
import tasks_list

def create_tasks_list(self):
    try:
      # Ask user To Enter Task Name
      print("Enter TasksList Name, please:")
      task_name = input()

      new_task = tasks_list.TasksListc(task_name.strip())

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
    print("Existing TasksLists:\n")
    i = 1
    for task in self.tasks_lists:
      print(f"{i}" + "\t" + task.name + " " + f"{task.date}" + "\n")
      i+=1
def deleteListsOptions(self):
    try:  
      print("Delete Options")
      print("Choose What do you want to delete?")
      print("1. Delete Tasks Lists")
      print("2. Delete Specific Tasks List")
      print("3. Cancel")
      delete_option = int(input())
      if delete_option == 1:
        helper_methods.deleteGeneralList(self.tasks_lists)
      elif delete_option == 2:
        self.print_tasks_list_info()
        print("Enter TasksList Title You Wanna Delete")
        inputTitle = input()
        delete_specific_task_list(inputTitle, self.tasks_lists)
      elif delete_option == 3:
        print("Cancel...")
      else:
        print("Invalid Input")

    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)



def delete_specific_task_list(title, list):
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
      tasks_list_name = input()
      is_tasks_list_name_exist = False
      index = 0
      for tasksList in self.tasks_lists:
        if tasks_list_name.lower() == tasksList.name.lower():
          is_tasks_list_name_exist = True
          break
        index += 1

      if is_tasks_list_name_exist:
        print("Enter Task Name:")
        taskName = input()
        
        task = Task(taskName.strip()) 
        self.tasks_lists[index].tasks.append(task)
        print(taskName, "Task Has Been Created And Added To the chosen TasksList")

      else:
        print("No existing TasksList With Such Name:", tasks_list_name)
        return
      

    
      # I Should update the list, but first let us test it 
      with shelve.open("local_storage") as db:
         db['tasks_lists'] = self.tasks_lists
         print("Added Tasks Has Been Saved...")
         
    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number:", error_info.lineno)   
    
def print_tasks_list_with_their_tasks(self):
  print("Existing TasksLists:\n")
  i = 1
  t = 1
  index = 0
  task_index = 0
  for tasksList in self.tasks_lists:
    print(f"{i}" + "\t" +  tasksList.name + f"\t{tasksList.date}\n")
    while task_index < len(self.tasks_lists[index].tasks):
       print(f"\t{t}", self.tasks_lists[index].tasks[task_index].name, self.tasks_lists[index].tasks[task_index].date)
       t += 1
       task_index +=1
    print()
    index += 1
    task_index = 0
    t = 1
    i+=1

def add_tasks_list(self, name):
   added_tasks_list = tasks_list.TasksListc(name)
   self.tasks_lists.append(added_tasks_list)
   with shelve.open("local_storage") as db:
      db['tasks_lists'] = self.tasks_lists
      print(f"tasks_lists '{name}' has been added" )