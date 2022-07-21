'''
Global arguments
'''
import os 

# maximum filesize in megabytes
file_mb_max = 100
# encryption key
app_key = 'any_non_empty_string'
# full path destination for our upload files
upload_dest = os.path.join(os.getcwd(), 'uploads_folder')
# list of allowed allowed extensions
extensions = set(['csv','jpg','jpeg','txt', 'pdf', 'png', 'tiff','gtiff'])

'''
 Refered from https://towardsdatascience.com/writing-a-multi-file-upload-python-web-app-with-user-authentication-8f75064b819a#:~:
 text=To%20do%20this%20we%20run%20the%20python%20script%2C,app.%20Adding%20an%20encrypted%20database%20for%20user%20authentication
'''