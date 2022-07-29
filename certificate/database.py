import pymongo

from dotenv import load_dotenv
import os

import certificate
 
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

def find_user(certificate_id):
    try:
        # print(certificate_id)
        found_user = user.find_one({ "certificate_id": certificate_id})
        # print(found_user)
        return found_user
        # return found_user['name'],found_user['image_path'],found_user['variableData']
    except TypeError:
        return None

def find_certificates(email):
    try:
        certificates_array = []
        user_datas = user.find({ "email": email}, { "certificate_link":1})
        for user_data in user_datas:
            certificate_link = user_data['certificate_link']
            certificates_array.append(certificate_link)

        print(certificates_array)
        # return ''.join(certificates_array)
        return certificates_array
    except TypeError:
        return None
def users_mails(image_path):
    try:
        email_certificate_link_array = []
        user_datas = user.find({ "image_path": image_path}, { "email":1, "certificate_link":1})
        for user_data in user_datas:
            email = user_data['email']
            certificate_link = user_data['certificate_link']
            email_certificate_link_array.append([email, certificate_link])
            # certificate_link_array.append(certificate_link, )
        print(email_certificate_link_array)
        # return (''.join(email_array),''.join(certificate_link_array))
        return email_certificate_link_array
    except TypeError:
        return None
