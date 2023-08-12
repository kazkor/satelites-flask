from flask import Flask,request,render_template,jsonify
from model import get_model, get_pred,get_classes, file_handler
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():

    data = data = {"pred": "",
                    "max": "" }
    return render_template('index.html',user_data = data)

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    file_handler(file)

    predictions = get_pred(model=model, image_path="app/static/temporary/perm.png")

    index_of_max_value = np.argmax(predictions)

    data = {"pred":str(predictions),
                    "max": f"{class_names[str(index_of_max_value)]}: {np.argmax(predictions)} "}
    
    return render_template('index.html', user_data=data)


if __name__ == '__main__':
    class_names = get_classes()
    model = get_model()
    app.run(debug=True,port=8000)