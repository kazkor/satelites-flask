from flask import Flask, request, render_template, jsonify, url_for
from model import get_model, get_pred,get_classes, file_handler
import numpy as np
import time
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():

    predictions = [0 for _ in range(20)]
    
    data = data = {"pred": str(predictions),
                    "class_names":class_names,
                    "max": "",
                    "max_value":"" }
                    
    return render_template('index.html',user_data = data)

@app.route('/upload', methods=['POST'])
def upload_file():
    
    file = request.files['file']
    
    file_path, file_name = file_handler(file)

    predictions, index_of_max_value, max_value = get_pred(model=model, image_path=file_path)

    data = {
        "pred": str(predictions),
        "class_names": class_names,
        "uploaded_image": url_for('static', filename=f'temporary/{file_name}'),
        "max": f"{class_names[str(index_of_max_value)]}",
        "max_value":max_value
    }
    
    return render_template('index.html', user_data=data)


if __name__ == '__main__':

    class_names = get_classes()
    model = get_model()
    app.run(debug=True,port=8000)