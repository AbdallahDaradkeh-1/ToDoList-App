import tasks_list_logic, load_data



class ToDoListOperations:
  def __init__(self):
    self.tasks_lists = []
    load_data.load_tasks_list_data(self)

  def load_tasks_list_data(self):
    load_data.load_tasks_list_data(self)

  def add_tasks_list(self, name):
    tasks_list_logic.add_tasks_list(self, name)

  def save_changed_tasks_list_name(self, name):
    tasks_list_logic.save_changed_tasks_lists_name(self, name)
  def change_tasks_lists_name(self, name, id):
    tasks_list_logic.change_tasks_lists_name(self, name, id)

  def create_tasks_list(self):
    tasks_list_logic.create_tasks_list(self)

  def print_tasks_list_info(self):
    tasks_list_logic.print_tasks_list_info(self)

  def deleteListsOptions(self):
   tasks_list_logic.deleteListsOptions(self)

  def FindSpecificTaskList(self):
    tasks_list_logic.FindSpecificTaskList(self, self.tasks_lists)
  def add_task_to_specific_tasks_list(self):
    tasks_list_logic.add_task(self)
  def print_tasks_list_with_their_tasks(self):
    tasks_list_logic.print_tasks_list_with_their_tasks(self)






# Quick Test
