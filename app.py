from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "model/model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class labels
CLASS_NAMES = ["Bacterial spot rot", "Black Rot", "Downy Mildew","No disease"] 

# Preprocess the image
def preprocess_image(image):
    image = image.resize((256, 256))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded file
        file = request.files["image"]
        if not file:
            return render_template("index.html", error="Please upload an image.")
        
        # Preprocess and predict
        image = Image.open(file)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = CLASS_NAMES[np.argmax(prediction)]

        return render_template("result.html", class_name=predicted_class)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
