import os
from flask import Flask, flash, redirect, render_template, request
from certificate import config
from certificate.generator import generate 
# from certificate.config import file_mb_max, upload_dest, extensions
# from templates import upload
app = Flask(__name__)

if not os.path.isdir(config.upload_dest):
    os.mkdir(config.upload_dest)

# config['MAX_CONTENT_LENGTH'] = config.file_mb_max * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.extensions
# @app.route('/')
# def upload():
    
@app.route('/', methods=['GET','POST'])
def upload_post():
    if request.method == 'POST':
        # csv = request.files["csv"]
        if 'csv' not in request.files:
            # flash('No files found, try again.')
            return redirect(request.url)    
        # file = request.files.getlist('files[]')    
        csv_file = request.files["csv"]
        # for csv_file in files:
        if csv_file and allowed_file(csv_file.filename):
            # filename = secure_filename(csv_file.filename)
            print(csv_file.filename)
            csv_file.save(os.path.join( config.upload_dest, csv_file.filename))    
            # flash('File(s) uploaded')
        img_file = request.files["image"]
        # for img_file in files:
        if img_file and allowed_file(img_file.filename):
            # filename = secure_filename(img_file.filename)
            print(img_file.filename)
            img_file.save(os.path.join( config.upload_dest, img_file.filename)) 
            #print(type(os.path.join( config.upload_dest, img_file.filename)))
            val = generate(os.path.join( config.upload_dest, img_file.filename), ['manish','prince'],['H2S0SSDS00001','H2S0SSDS00002'],config.upload_dest)
            print(val)
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
def server():
    app.run(debug=True)

if __name__ == '__main__':
    print("Working")
    server()