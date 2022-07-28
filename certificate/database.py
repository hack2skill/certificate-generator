import pymongo

from dotenv import load_dotenv
import os
 
# Use load_env to trace the path of .env:
load_dotenv('.env') 
 
# Get the values of the variables from .env using the os library:
MONGO_URI = os.environ.get("MONGO_URI")

database = pymongo.MongoClient(MONGO_URI)["certificate"]

user = database["users"]
event = database["events"]
#print(type(user))
def save_data(data):
    saved_user = user.insert_one(data)
    return saved_user

def find_save_data(data):
    saved_user = user.find_one_and_update(data)
    return saved_user

def find_user(certificate_id):
    print(certificate_id)
    found_user = user.find_one({ "certificate_id": certificate_id})
    print(found_user)
    return found_user['name'],found_user['image_path'],found_user['name_origin_coordinates'],found_user['certificate_id_origin_coordinates'],