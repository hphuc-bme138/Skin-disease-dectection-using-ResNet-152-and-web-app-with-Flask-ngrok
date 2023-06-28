from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join('./static', 'uploads')

print(UPLOAD_FOLDER)
app = Flask(__name__,
            static_folder='./static', # sửa lại theo GG drive của anh 
            template_folder='./templates') # sửa lại theo GG drive của anh

@app.route('/', methods=(["GET", 'POST']))
def home():
    if request.method == 'POST':
      uploaded_img = request.files['uploaded-file']
      img_filename = secure_filename(uploaded_img.filename)
      uploaded_img.save(os.path.join(UPLOAD_FOLDER, img_filename))
      return render_template('home.html', user_image = '/static/uploads/' + img_filename, predict_label = 'Label') # predict_label la ket qua
    
    return render_template('home.html', predict_label = '')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skin-lesion')
def lesion():
    return render_template('lesion.html')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)