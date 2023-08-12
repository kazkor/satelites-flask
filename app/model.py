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
    return load_model('app/models/model_128.h5')


def get_classes():
    # Wczytanie danych z pliku JSON
    with open("app/static/class_labels.json", 'r') as json_file:
        loaded_data = json.load(json_file)

    # Teraz 'loaded_data' zawiera wczytane dane jako słownik
    return loaded_data


def file_handler(file_storage):
    # Assuming 'file_storage' is the FileStorage object representing the uploaded file
    uploaded_file = file_storage

    # Get the binary content of the uploaded file
    file_content = uploaded_file.read()

    # Securely generate a filename for the saved picture
    filename = "perm.png"

    # Choose a directory to save the picture
    save_directory = "temporary/"

    # Combine the directory and filename to get the full path
    full_path = os.path.join(save_directory, filename)

    # Check if the uploaded file is an image (you might want to improve this check)
    if uploaded_file.content_type.startswith('image/'):
        # Open the image using Pillow
        img = Image.open(io.BytesIO(file_content))

        # Convert the image to PNG format
        if img.format != 'PNG':
            img = img.convert('RGBA')  # Convert to RGBA if needed
            img.save(full_path, format='PNG')
        else:
            img.save(full_path)

    else:
        # Handle non-image files here
        print("Uploaded file is not an image.")

    # Now the picture is saved as PNG at the specified location
