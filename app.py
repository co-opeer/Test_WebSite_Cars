import os

import requests
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from templates.test_on_dataset import predict_car


app = Flask(__name__)
# Визначте шлях до каталогу UPLOAD_FOLDER
upload_folder = os.path.abspath('static/uploads')

# Перевірте, чи існує каталог, і створіть його, якщо він не існує
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

# Налаштуйте налаштування UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = upload_folder


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = predict_car(file_path)
            return render_template('result.html', result='Car' if result else 'No Car')
@app.route('/home')
def home():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

