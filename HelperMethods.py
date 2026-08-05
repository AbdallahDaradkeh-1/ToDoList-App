import shelve


def deleteGeneralList(self, list):
      i = 0
      if len(list) == 0:
        print("This List Is Empty")

      list.clear()
        
      with shelve.open("local_storage") as db:
          db["tasks_lists"] = list
          print("This List Updates Have Been Saved")