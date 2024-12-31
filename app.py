from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import gdown  # For downloading from Google Drive
import os

app = Flask(__name__)

# Google Drive model link (replace with your shareable link)
MODEL_DRIVE_URL = "https://drive.google.com/uc?id=1bCwZYkfX0YxG3B6kva5zdIqer97pKn4X"
MODEL_PATH = "./model1.h5"

# Define class labels
class_names = ["Bacterial spot rot", "Black Rot", "Downy Mildew", "No disease"]

# Function to download the model from Google Drive
def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Google Drive...")
        gdown.download(MODEL_DRIVE_URL, MODEL_PATH, quiet=False)
    else:
        print("Model already exists locally.")

# Load the model
def load_model():
    download_model()
    print("Loading the model...")
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# Preprocess the image
def preprocess_image(image):
    image = image.resize((256, 256))  # Resize to model input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["image"]
        if not file:
            return render_template("index.html", error="Please upload an image.")

        # Process the uploaded image
        image = Image.open(file)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = round(100 * np.max(prediction), 2)

        return render_template(
            "result.html", prediction=predicted_class, confidence=confidence
        )
    except Exception as e:
        print(f"Error: {e}")
        return render_template("index.html", error="An error occurred during prediction.")

if __name__ == "__main__":
    app.run(debug=True)

