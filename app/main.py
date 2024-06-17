from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

main = Blueprint('main', __name__)

model = load_model('model/model.h5')

def preprocess_image(image):
    image = image.resize((80, 60))  # Adjust size to match your model's input
    image = np.array(image) / 255.0  # Normalize image

    if len(image.shape) == 2:  # Grayscale to RGB
        image = np.stack((image,) * 3, axis=-1)
    elif image.shape[2] == 4:  # Remove alpha channel if present
        image = image[:, :, :3]

    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@main.route('/', methods=['POST'])
def main_route():
    try:
        image = Image.open('app/static/Image.jpeg')
        preprocessed_image = preprocess_image(image)
        prediction = model.predict(preprocessed_image)

        is_blurry = bool(prediction[0][0] < 0.5)

        return jsonify({
            "is_blurry": is_blurry,
            "percentage": "{:.2f}".format(prediction[0][0] * 100) + "%"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
