
from datetime import date

class TasksListc:
  def __init__(self, name):
    self.name = name
    self.date = date.today()
    self.tasks = []
