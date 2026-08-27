from tkinter import *
from tkinter import ttk

def screen_configurations():
   root = Tk()
   root.geometry("800x600")
   return root

def tasks_lists_form(frame, operations_object):
  
  
  custom_row = 0

  these_tasks_lists = operations_object.tasks_lists
  print(f"TaskList: {these_tasks_lists}")

  for tasks_list in these_tasks_lists:
      entry = ttk.Entry(frame)
      entry.insert(0, tasks_list.name)
      entry.config(state="readonly")
      entry.grid(sticky='e', column=0, row=custom_row, padx=50)
      edit_action = ttk.Button(
        frame,
        text="Edit",
        command=lambda task=tasks_list, new_entry = entry: edit_task_list(task, new_entry)
      )
      edit_action.grid( row=custom_row, sticky='e')

      custom_row += 1
  custom_row = 0
  for tasks_list in these_tasks_lists:
      entry = ttk.Entry(frame,)
      entry.insert(0, tasks_list.date)
      entry.config(state="readonly")
      entry.grid(sticky='e', column=2, row=custom_row)

      custom_row += 1


def edit_task_list(task, entry):
    print("Clicked:", task.name)
    print("Task object:", task)
    entry.config(state = "normal")
    entry.select_range(0, "end")
