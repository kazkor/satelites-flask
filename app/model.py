from keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json
import os
import io
from werkzeug.utils import secure_filename
from PIL import Image

def get_pred(model):
    image_path = ""
    img = image.load_img(image_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    return predictions


def get_pred(model,image_path):
    img = image.load_img(image_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    return predictions


def get_model():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "models", "model_128.h5")
    return load_model(model_path)


import os

def get_classes():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    class_labels_path = os.path.join(script_dir, "static", "class_labels.json")

    # Load data from the JSON file
    with open(class_labels_path, 'r') as json_file:
        loaded_data = json.load(json_file)

    return loaded_data



def file_handler(file_storage):
    uploaded_file = file_storage
    file_content = uploaded_file.read()
    filename = "perm.png"
    save_directory = "app/static/temporary/"
    full_path = os.path.join(save_directory, filename)

    # Create the 'temporary' directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    if uploaded_file.content_type.startswith('image/'):
        img = Image.open(io.BytesIO(file_content))
        if img.format != 'PNG':
            img = img.convert('RGBA')
            img.save(full_path, format='PNG')
        else:
            img.save(full_path)
    else:
        print("Uploaded file is not an image.")

    # Now the picture is saved as PNG at the specified location
