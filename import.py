from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json
from glob import glob

## Connecting to mongo

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.zgb8ts
# specify a collection
collection = db.generated


## Listing Files
# Like this:
path = "/workspace/ds2002-dp2/data/"


# or this:
for (roots, dirs, file) in os.walk(path):
    for f in file:
        print(f)
        
list_file= os.listdir(path)



# for file in list_file:
#     if file.endswith(".json"):
#         with open(os.path.join(file)) as jsonfiles:
#             file_data = json.load(file)
#             print(file_data)

try:
    for file in glob("/workspace/ds2002-dp2/data/*.json"):
        jsonfiles= []
        with open(file, 'r') as jsonfile:
            jsonfiles.append(json.load(jsonfile))
            print(jsonfiles)
except Exception as e:
      print(e, "error when loading", f)

jsonfiles2= dict(jsonfiles)
if isinstance(jsonfiles2, list):
    try:
        collection.insert_many(jsonfiles2)
    except Exception as e:
            print(e, "when importing into Mongo")  
else:
    try:
        collection.insert_one(jsonfiles2)
    except Exception as e:
        print(e)

        
      

     

get_record = db.generated.count_documents({} )
print(dumps(get_record, indent=2))

## Importing 

# Loading or Opening the json file
# with open('data.json') as file:
#     file_data = json.load(file)


# if isinstance(file_data, list):
#     collection.insert_many(file_data)  
# else:
#     collection.insert_one(file_data)
# except Expection as e:
#     print("Error": e)