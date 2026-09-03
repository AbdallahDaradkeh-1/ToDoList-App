from tkinter import *
from tkinter import ttk
from tasks_list_logic import add_tasks_list
def screen_configurations():
   root = Tk()
   root.geometry("800x600")
   return root

def tasks_lists_form(frame, operations_object):
  
  
  custom_row = 0
  these_tasks_lists = operations_object.tasks_lists

  for tasks_list in these_tasks_lists:
      entry = ttk.Entry(frame)
      entry.insert(0, tasks_list.name)
      entry.config(state="readonly")
      entry.grid(sticky='e', column=0, row=custom_row, padx=50)
      edit_action = ttk.Button(
        frame,
        text="Edit")
      tasks_list_id = tasks_list.id
      edit_action.config(command=lambda new_entry = entry, edit_action = edit_action, the_frame = frame, action_row = custom_row, operations_object =operations_object, tasks_list_id = tasks_list_id : edit_task_list(new_entry,edit_action, the_frame, action_row, operations_object, tasks_list_id)
            )
      edit_action.grid( row=custom_row, sticky='e')
      delete_action = ttk.Button(
          frame,
          text="Delete"
      )
      delete_action.grid(row=custom_row, sticky='e', column= 4)
      delete_action.config(command= lambda tasks_list_id = tasks_list_id, the_frame = frame : delete_task_list(tasks_list_id, the_frame, operations_object))
      

      custom_row += 1
  custom_row = 0
  for tasks_list in these_tasks_lists:
      entry = ttk.Entry(frame,)
      entry.insert(0, tasks_list.date)
      entry.config(state="readonly")
      entry.grid(sticky='e', column=3, row=custom_row)

      custom_row += 1


def edit_task_list(new_entry, edit_action, the_frame, action_row, operations_object, tasks_list_id):
    new_entry.config(state = "normal")
    new_entry.focus_set()
    new_entry.select_range(0, END)
    edit_action.grid_remove()
    save_button = ttk.Button(the_frame, text="Save")
    save_button.grid(row=action_row, sticky='e')
    cancel_button = ttk.Button(the_frame, text="Cancel")
    cancel_button.grid(row=action_row, column=2)
    # entry.grid_configure()

    save_button.config(command= lambda entry = new_entry, save_button = save_button, cancel_button = cancel_button, operations_object= operations_object, edit_action = edit_action, tasks_list_id = tasks_list_id : save_new_task_list(entry, save_button, cancel_button, operations_object, edit_action, tasks_list_id))

def delete_task_list(tasks_list_id, the_frame, operations_object):
    operations_object.delete_task_list(tasks_list_id)
    refresh_tasks_list(operations_object, the_frame)
    


def save_new_task_list(entry, save_button, cancel_button, operations_object, edit_action, tasks_list_id):  
    task_name = entry.get()

    operations_object.change_tasks_lists_name(task_name, tasks_list_id)
    save_button.grid_remove()
    cancel_button.grid_remove()
    edit_action.grid_configure()
    entry.config(state='readonly')
    



def create_tasks_list_form(frame, operations_object, tasks_list_frame):
    
  create_label = ttk.Label(frame, text="Create A TaskList Title")
  tasks_list_subject = ttk.Entry(frame)
  create_button = ttk.Button(
    frame,
    text="Create",
    command= lambda: save_task_list(tasks_list_subject, operations_object, tasks_list_frame)
  )


  create_label.grid(padx=5, pady=5)
  tasks_list_subject.grid(padx=5)
  create_button.grid(row=1,column=1)

def save_task_list(subject, operations_object, frame):
  task_title_value = subject.get()
  if task_title_value:
       operations_object.add_tasks_list(task_title_value)
       subject.delete(0, END)

     
  refresh_tasks_list(operations_object, frame)


def refresh_tasks_list(operations_object, frame):
  for widget in frame.winfo_children():
    widget.destroy()

  these_tasks_lists = operations_object.tasks_lists
  custom_row = 0

  for tasks_list in these_tasks_lists:
                entry = ttk.Entry(frame)
                entry.insert(0, tasks_list.name)
                entry.config(state="readonly")
                entry.grid(sticky='e', column=0, row=custom_row, padx=50)
                edit_action = ttk.Button(
                  frame,
                  text="Edit")
                tasks_list_id = tasks_list.id
                edit_action.config(command=lambda new_entry = entry, edit_action = edit_action, the_frame = frame, action_row = custom_row, operations_object =operations_object, tasks_list_id = tasks_list_id : edit_task_list(new_entry,edit_action, the_frame, action_row, operations_object, tasks_list_id)
                      )
                edit_action.grid( row=custom_row, sticky='e')
                delete_action = ttk.Button(
                    frame,
                    text="Delete"
                )
                delete_action.grid(row=custom_row, sticky='e', column= 4)
                delete_action.config(command= lambda tasks_list_id = tasks_list_id, the_frame = frame : delete_task_list(tasks_list_id, the_frame, operations_object))
    
                custom_row += 1
    
  custom_row = 0
  for tasks_list in these_tasks_lists:
    entry = Entry(frame,)
    entry.insert(0, tasks_list.date)
    entry.config(state="readonly")
    entry.grid(sticky='e', column=1, row=custom_row)

    custom_row += 1 

