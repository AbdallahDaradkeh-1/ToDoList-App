from tkinter import *
from ToDoListOperations import ToDoListOperations

operations = ToDoListOperations()

thisTasksList = []



thisTasksList = operations.tasks_lists


root = Tk()

root.geometry("800x600")

taskListLabel = Label(root, text = "TaskLists", font='bold')
taskListLabel.grid(column=0, row=0)

frame = Frame(root, )
frame.grid(column=1,row=1)
customRow = 0
for tasksList in thisTasksList:
  label = Label(frame,text=f"{tasksList.name}")
  label.grid(sticky='e', column=0, row=customRow, padx=50)

  customRow += 1
customRow = 0
for tasksList in thisTasksList:
  label = Label(frame,text=f"{tasksList.date}")
  label.grid(sticky='e', column=1, row=customRow)

  customRow += 1




root.mainloop()