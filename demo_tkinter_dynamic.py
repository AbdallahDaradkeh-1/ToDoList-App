from tkinter import *
from to_do_list_operations import ToDoListOperations
from tkinter import ttk
from tkinter_functions import screen_configurations
from tkinter_tasks_list_operations import save_task_list

operations = ToDoListOperations()


root = screen_configurations()

tasks_list_header_label = Label(root, text = "TaskLists", font='bold')
tasks_list_header_label.grid(column=0, row=0)

create_frame = Frame(root, padx=10, pady=10, background="yellow")
create_frame.grid()

tasks_list_subject = Entry(create_frame)



create_task_label = ttk.Label(create_frame, text="Add A TaskList Title")
submit_task_list_button = ttk.Button(
  create_frame,
  text="Add",
  command= lambda: save_task_list(tasks_list_subject, operations, tasks_list_frame)
)

submit_task_list_button.grid()


create_task_label.grid()
tasks_list_subject.grid()




tasks_list_frame = Frame(root)
tasks_list_frame.grid()

custom_row = 0

these_tasks_lists = operations.tasks_lists

for tasks_list in these_tasks_lists:
    entry = ttk.Entry(tasks_list_frame,)
    entry.insert(0, tasks_list.name,)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=0, row=custom_row, padx=50)
    edit_action = ttk.Button(
       tasks_list_frame,
       text="Edit",
       command=lambda task=tasks_list, new_entry = entry: edit_task_list(task, new_entry)
    )
    edit_action.grid( row=custom_row, sticky='e')

    custom_row += 1
custom_row = 0
for tasks_list in these_tasks_lists:
    entry = ttk.Entry(tasks_list_frame,)
    entry.insert(0, tasks_list.date)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=2, row=custom_row)

    custom_row += 1


def edit_task_list(task, entry):
    print("Clicked:", task.name)
    print("Task object:", task)
    entry.config(state = "normal")
    entry.select_range(0, "end")




root.mainloop()