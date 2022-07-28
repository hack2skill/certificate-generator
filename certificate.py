import os
from datetime import date
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request
from certificate import config
from certificate.csv_reading import read_csv
from certificate.database import find_user, save_data
from certificate.generator import generate
from certificate.image_upload import upload_to_aws 
from flask_cors import CORS, cross_origin

# from certificate.config import file_mb_max, upload_dest, extensions
# from templates import upload
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
 
# Use load_env to trace the path of .env:
load_dotenv('.env') 
 
# Get the values of the variables from .env using the os library:
BASE_URL = os.environ.get("DOMAIN")
if not os.path.isdir(config.upload_dest):
    os.mkdir(config.upload_dest)

# config['MAX_CONTENT_LENGTH'] = config.file_mb_max * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.extensions
# @app.route('/')
# def upload():
    
@app.route('/', methods=['GET','POST'])
@cross_origin()
def upload_post():
    if request.method == 'POST':
        # csv = request.files["csv"]
        name = request.form.get('name')
        certificate_id = request.form.get('certificateId')
        print(certificate_id,name)
        image_path = ''
        img_file = request.files["file"]
        print(img_file)
        # for img_file in files:
        if img_file and allowed_file(img_file.filename):
            # filename = secure_filename(img_file.filename)
            #print(img_file.filename)
            image_path = img_file.filename
            img_file.save(os.path.join(config.upload_dest, img_file.filename))
            user = dict()
            user['image_path'] = image_path
            saved_data = save_data(user)
            print(saved_data)
            # image = upload_to_aws(os.path.join(config.upload_dest, img_file.filename))
            # print(image)
            # while True:
            #     pass
            #print(type(os.path.join( config.upload_dest, img_file.filename)))
            # val = generate(os.path.join( config.upload_dest, img_file.filename), ['manish','prince'],['H2S0SSDS00001','H2S0SSDS00002'],config.upload_dest)
            # print(val)
        # if 'csv' not in request.files:
        #     # flash('No files found, try again.')
        #     return redirect(request.url)    
        # # file = request.files.getlist('files[]')    
        # csv_file = request.files["csv"]
        # # for csv_file in files:
        # if csv_file and allowed_file(csv_file.filename):
        #     # filename = secure_filename(csv_file.filename)
        #     #print(csv_file.filename)
        #     csv_file.save(os.path.join( config.upload_dest, csv_file.filename))  
        #     data = read_csv(os.path.join(config.upload_dest, csv_file.filename))
        #     for i in range(1,len(data)):
        #         # print(data[i])
        #         user = dict()
        #         for j in range(len(data[0])):
        #             user[data[0][j]] = data[i][j]

        #         #print(user)
        #         user['image_path'] = image_path
        #         cert_id = user['certificate_id']
        #         print(BASE_URL,cert_id)
        #         user['certificate_link'] = f'{BASE_URL}/api/{cert_id}'
        #         # Returns the current local date
        #         today = date.today()
        #         user['date_of_issue'] = str(today)
        #         saved_data = save_data(user)
        #         print(saved_data)

        #     # flash('File(s) uploaded')
        # return redirect('/')
        # image = request.form.get("image")
        # print("hi",csv)
        # return redirect("/")
        # return redirect("/generate")

    return render_template("upload.html")

# @app.route("/")

@app.route('/csv_upload', methods=['POST'])
@cross_origin()
def upload_csv():
    if request.method == 'POST':
        if 'csv' not in request.files:
            return redirect(request.url)    
        csv_file = request.files["csv"]
        print(csv_file)
        if csv_file and allowed_file(csv_file.filename):
            # filename = secure_filename(csv_file.filename)
            #print(csv_file.filename)
            csv_file.save(os.path.join( config.upload_dest, csv_file.filename))  
            data = read_csv(os.path.join(config.upload_dest, csv_file.filename))
            for i in range(1,len(data)):
                # print(data[i])
                user = dict()
                for j in range(len(data[0])):
                    user[data[0][j]] = data[i][j]

                #print(user)
                # user['image_path'] = image_path
                cert_id = user['certificate_id']
                print(BASE_URL,cert_id)
                user['certificate_link'] = f'{BASE_URL}/api/{cert_id}'
                # Returns the current local date
                today = date.today()
                user['date_of_issue'] = str(today)
                saved_data = save_data(user)
                print(saved_data)

            # flash('File(s) uploaded')
        return redirect('/')
        # image = request.form.get("image")
        # print("hi",csv)
        # return redirect("/")
        # return redirect("/generate")

    return render_template("upload.html")
# @app.route('/generate', methods=['GET','POST'])
# def generate_certificate():
#     if request.method == 'POST':
#         csv = request.files["csv"]
#         # image = request.form.get("image")
#         print("hi",csv)

#         return redirect("/generate")
#     return render_template("generate.html")
@app.route('/api/<certificate_id>')
def show_image(certificate_id):
    name, image_path, name_origin_coordinates, certificate_id_origin_coordinates = find_user(certificate_id)
    # value = generate(f"uploads_folder/{image_path}", name, certificate_id, name_origin_coordinates = (650, 2650), certificate_id_origin_coordinates = (2100, 3600))
    value = generate(f"uploads_folder/{image_path}", name, certificate_id, name_origin_coordinates= name_origin_coordinates, certificate_id_origin_coordinates = certificate_id_origin_coordinates)
    print(value)
    
    return(certificate_id)
    
def server():
    app.run(debug=True)

if __name__ == '__main__':
    print("Working")
    server()