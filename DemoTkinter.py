from tkinter import *
from ToDoListOperations import ToDoListOperations

operations = ToDoListOperations()

thisTasksList = []



thisTasksList = operations.tasks_lists


root = Tk()

root.geometry("800x600")
tasksListName = Entry(root)
tasksListName.grid(column=0,row=0)

for tasksList in thisTasksList:
  label = Label(root,text=f"{tasksList.name} {tasksList.date}")
  label.grid()


root.mainloop()