from tkinter import *


def refresh_tasks_list(operations_object, frame):
  for widget in frame.winfo_children():
    widget.destroy()

  these_tasks_lists = operations_object.tasks_lists
  custom_row = 0

  for tasks_list in these_tasks_lists:
    entry = Entry(frame,)
    entry.insert(0, tasks_list.name,)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=0, row=custom_row)
    
    

    custom_row += 1
  custom_row = 0
  for tasks_list in these_tasks_lists:
    entry = Entry(frame,)
    entry.insert(0, tasks_list.date)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=1, row=custom_row)

    custom_row += 1 

def save_task_list(subject, operations_object, frame):
  task_title_value = subject.get()
  if task_title_value:
       operations_object.add_tasks_list(task_title_value)
       subject.delete(0, END)

     
  refresh_tasks_list(operations_object, frame)