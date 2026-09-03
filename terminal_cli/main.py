import traceback

from to_do_list_operations import ToDoListOperations


class Main:
  def __init__(self):
    self.operations = ToDoListOperations()

  def show_menu(self):
    self.options_number = 0
    print("1. Create Tasks List")
    self.options_number += 1
    print("2. Print Tasks Info")
    self.options_number += 1
    print("3. Delete Options Choices")
    self.options_number += 1
    print("4. Search For Specific TasksList")
    self.options_number += 1
    print("5. Add a task For Specific TasksList")
    self.options_number += 1
    print("6. Print TasksLists With Their Tasks Info")
    self.options_number += 1

    print("-1. Exit Program")
    


  def start(self):
    while True:
      try:  

          print("Welcome, Enter Operation Number You Want To Perform:")
          self.show_menu()
          operation_number = int(input())
          if operation_number == 1:
            self.operations.create_tasks_list()
          elif operation_number == 2:      
            self.operations.print_tasks_list_info()
          elif operation_number == 3:
            self.operations.delete_lists_options()
          elif operation_number == 4:
            self.operations.find_specific_task_list()
          elif operation_number == 5:
            self.operations.add_task_to_specific_tasks_list()
          elif operation_number == 6:
            self.operations.print_tasks_list_with_their_tasks()
          elif operation_number == -1:      
            print("Exiting Program...")
            return
          else:
            print("Invalid Input, Out Of Range!")
          
      except Exception as error:
        error_info = traceback.extract_tb(error.__traceback__)[-1]
        print("Error Type:", type(error).__name__)
        print("Error Message:", error)
        print("Line Number", error_info.lineno)


