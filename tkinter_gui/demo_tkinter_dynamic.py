from tkinter import *
from to_do_list_operations import ToDoListOperations
from tkinter import ttk
from .tkinter_functions import screen_configurations 
from .tkinter_functions import tasks_lists_form
from .tkinter_tasks_list_operations import create_tasks_list_form



operations = ToDoListOperations()
root = screen_configurations()

tasks_list_header_label = ttk.Label(root, text = "TaskLists", font='bold')
tasks_list_header_label.grid(column=0, row=0)

create_frame = Frame(root, padx=20, pady=20, background="grey")
create_frame.grid()

tasks_list_frame = Frame(root)
tasks_list_frame.grid()

create_tasks_list_form(create_frame, operations, tasks_list_frame)


tasks_lists_form(tasks_list_frame, operations)


root.mainloop()