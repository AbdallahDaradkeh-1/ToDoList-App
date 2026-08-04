import TasksListLogic

class ToDoListOperations:
  def __init__(self):
    self.tasks_lists = []

  def load_tasks_list_data(self):
    TasksListLogic.load_tasks_list_data(self)


  def create_tasks_list(self):
    TasksListLogic.create_tasks_list(self)

  def print_tasks_list_info(self):
    TasksListLogic.print_tasks_list_info(self)

  def deleteListsOptions(self):
   TasksListLogic.deleteListsOptions(self)

  def deleteGeneralList(self, list):
   TasksListLogic.deleteGeneralList(self, list)
  





# Quick Test
