from datetime import date

class Task:
  def __init__(self, name):
    self.name = name
    self.date = date
    self.priorities = [
      "High",
      "Mid",
      "Low"
    ]