from datetime import date

class Task:
  def __init__(self, name):
    self.name = name
    self.date = date.today()
    self.priorities = [
      "High",
      "Mid",
      "Low"
    ]