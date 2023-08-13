from keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json
import os
import io
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

def get_pred(model,image_path):
    img = image.load_img(image_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    index_of_max_value = np.argmax(predictions)

    max_value = np.max(predictions)

    return predictions, index_of_max_value, max_value


def get_model():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "models", "model_128.h5")
    return load_model(model_path)


def get_classes():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    class_labels_path = os.path.join(script_dir, "static", "class_labels.json")

    # Load data from the JSON file
    with open(class_labels_path, 'r') as json_file:
        loaded_data = json.load(json_file)

    return loaded_data


def file_handler(file):

     # Save the uploaded file to a temporary location
    file_name = secure_filename(file.filename)
    file_path = f'static/temporary/{file_name}'
    file.save(file_path)

    return file_path, file_name




