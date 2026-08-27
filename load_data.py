import shelve

def load_tasks_list_data(self):
    with shelve.open("local_storage") as db:  
      loaded_tasks_lists = db.get("tasks_lists", [])
      self.tasks_lists = loaded_tasks_lists
      print("Data Has Been Loaded")       