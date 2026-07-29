import traceback

from ToDoListOperations import ToDoListOperations


class Main:
  def __init__(self):
    self.operations = ToDoListOperations()

  def show_menu(self):
    self.optionsNumber = 0
    print("1. Create Tasks List")
    self.optionsNumber += 1
    print("2. Print Tasks Info")
    self.optionsNumber += 1

    print("-1. Exit Program")
    


  def start(self):
    try:  
      while True:
        self.operations.load_data()

        print("Welcome, Enter Operation Number You Want To Perform:")
        self.show_menu()
        operationNumber = int(input())
        if operationNumber == 1:
          self.operations.create_tasks_list()
        elif operationNumber == 2:      
          self.operations.print_tasks_list_info()
        elif operationNumber == -1:      
          print("Exiting Program...")
          return
        else:
          print("Invalid Input, Out Of Range!")
        



    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error Type:", type(error).__name__)
      print("Error Message:", error)
      print("Line Number", error_info.lineno)



main = Main()

main.start()