import os
import json

directory = "data"

for filename in os.listdir(directory):
  with open(os.path.join(directory, filename)) as f:
    print(f)
    # do other things with f

# assuming you have defined a connection to your db and collection already:

    # Loading or Opening the json file
    # try:
    #   file_data = json.load(f)
    # except Exception as e:
    #   print(e, "error when loading", f)
     
# Inserting the loaded data in the collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
    # if isinstance(file_data, list):
    #   try:
    #     collection.insert_many(file_data)
    #   except Exception as e:
    #     print(e, "when importing into Mongo")
    # else:
    #   try:
    #     collection.insert_one(file_data)
    #   except Exception as e:
    #     print(e)