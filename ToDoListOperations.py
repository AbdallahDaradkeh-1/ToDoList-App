import TasksListLogic, LoadData

class ToDoListOperations:
  def __init__(self):
    self.tasks_lists = []

  def load_tasks_list_data(self):
    LoadData.load_tasks_list_data(self)


  def create_tasks_list(self):
    TasksListLogic.create_tasks_list(self)

  def print_tasks_list_info(self):
    TasksListLogic.print_tasks_list_info(self)

  def deleteListsOptions(self):
   TasksListLogic.deleteListsOptions(self)

  def FindSpecificTaskList(self):
    TasksListLogic.FindSpecificTaskList(self, self.tasks_lists)
  def add_task_to_specific_tasks_list(self):
    TasksListLogic.add_task(self)






# Quick Test
