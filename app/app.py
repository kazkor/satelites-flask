from flask import Flask, request, render_template, jsonify, url_for
from model import get_model, get_pred,get_classes
import numpy as np
import time
import os
from werkzeug.utils import secure_filename


app = Flask(__name__, static_folder='static')

@app.route('/')
def home():

    data = data = {"pred": "",
                    "class_names":class_names,
                    "max": "" }
    return render_template('index.html',user_data = data)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    # Save the uploaded file to a temporary location
    filename = secure_filename(file.filename)
    file_path = f'static/temporary/{filename}'
    file.save(file_path)

    predictions = get_pred(model=model, image_path=file_path)
    
    index_of_max_value = np.argmax(predictions)

    data = {
        "pred": str(predictions),
        "class_names": class_names,
        "uploaded_image": url_for('static', filename=f'temporary/{filename}'),
        "max": f"{class_names[str(index_of_max_value)]}"
    }
    
    return render_template('index.html', user_data=data)


if __name__ == '__main__':

    class_names = get_classes()
    model = get_model()
    app.run(debug=True,port=8000)