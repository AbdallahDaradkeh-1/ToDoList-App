from tkinter import *
from to_do_list_operations import ToDoListOperations

operations = ToDoListOperations()

this_tasks_list = []





root = Tk()

root.geometry("800x600")

task_list_label = Label(root, text = "TaskLists", font='bold')


task_list_label.grid(column=0, row=0)

create_frame = Frame(root, padx=10, pady=10, background="yellow")
create_frame.grid()

task_title = Entry(create_frame)


def save_task_list():
  task_title_value = task_title.get()
  if task_title_value:
       operations.add_tasks_list(task_title_value)
       task_title.delete(0, END)

     
  refresh_tasks_list()

create_task_label = Label(create_frame, text="Add A TaskList Title")
submit_task_list_button = Button(
  create_frame,
  text="Add",
  command= save_task_list
)

submit_task_list_button.grid()


create_task_label.grid()
task_title.grid()




tasks_list_frame = Frame(root)
tasks_list_frame.grid()

custom_row = 0

this_tasks_list = operations.tasks_lists

for tasks_list in this_tasks_list:
    entry = Entry(tasks_list_frame,)
    entry.insert(0, tasks_list.name,)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=0, row=custom_row, padx=50)

    custom_row += 1
custom_row = 0
for tasks_list in this_tasks_list:
    entry = Entry(tasks_list_frame,)
    entry.insert(0, tasks_list.date)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=1, row=custom_row)

    custom_row += 1


def refresh_tasks_list():
  for widget in tasks_list_frame.winfo_children():
    widget.destroy()

  this_tasks_list = operations.tasks_lists
  custom_row = 0

  for tasks_list in this_tasks_list:
    entry = Entry(tasks_list_frame,)
    entry.insert(0, tasks_list.name,)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=0, row=custom_row, padx=50)

    custom_row += 1
  custom_row = 0
  for tasks_list in this_tasks_list:
    entry = Entry(tasks_list_frame,)
    entry.insert(0, tasks_list.date)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=1, row=custom_row)

    custom_row += 1





root.mainloop()