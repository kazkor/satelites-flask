from flask import Flask, request, render_template, jsonify, url_for, make_response
from model import get_model, get_pred,get_classes, file_handler,create_response
import numpy as np
import time
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'app/static/temporary'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home
@app.route('/')
def home():

    # blank predictions for index.html
    predictions = [0 for _ in range(20)]

    # creating response json
    data = data = {"pred": str(predictions),
                    "class_names":class_names,
                    "max": "",
                    "max_value":"" }
                    
    return render_template('index.html',user_data = data)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Upload
@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # fetching file from client request
        file = request.files['file']

        if file.filename == '':
            return jsonify({"error":"no file"})
            
        if file and allowed_file(file.filename):

            # handling a file
            file_path, file_name = file_handler(file)

            # getting predictions
            predictions, index_of_max_value, max_value = get_pred(model=model, image_path=file_path)

            # creating response
            data = create_response(predictions, class_names, file_name, index_of_max_value, max_value)
            
            return render_template('index.html', user_data=data)
        else:
            return jsonify({"error":"wrong file"})


@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({"error":"Not found"}),404)


if __name__ == '__main__':
    class_names = get_classes()
    model = get_model()
    app.run(debug=True,port=8001)