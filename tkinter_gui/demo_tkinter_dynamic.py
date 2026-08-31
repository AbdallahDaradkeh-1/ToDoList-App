from tkinter import *
import tkinter as tk
from to_do_list_operations import ToDoListOperations
from tkinter import ttk
from .tkinter_functions import screen_configurations 
from .tkinter_functions import tasks_lists_form
from .tkinter_tasks_list_operations import create_tasks_list_form



operations = ToDoListOperations()
root = screen_configurations()

canvas = tk.Canvas(root, width= 700, height=600)
canvas.pack(side='left', fill='both', expand='True')
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
# tasks_list_header_label = ttk.Label(root, text = "TaskLists", font='bold')
# tasks_list_header_label.pack()

content_frame = Frame(canvas)
content_frame.pack()


create_frame = Frame(content_frame, padx=20, pady=20, background="grey")
create_frame.pack(fill='x')
canvas.create_window((0,0), window=content_frame, anchor='nw')
content_frame.bind(
    "<Configure>",
    lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
)
tasks_list_frame = Frame(content_frame)
tasks_list_frame.pack()

tasks_list_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

create_tasks_list_form(create_frame, operations, tasks_list_frame)

# print(tasks_list_header_label.keys)
tasks_lists_form(tasks_list_frame, operations)
# for option in create_frame.keys():
#     print(f"{option}: {create_frame.cget(option)}")

root.mainloop()