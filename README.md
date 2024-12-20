# CauliCare 🌿

CauliCare is a web application that helps farmers and agricultural enthusiasts diagnose cauliflower diseases using deep learning. Users can upload an image of a cauliflower leaf, and the model predicts the disease affecting it.

## Features
- **Image Upload**: Upload images of cauliflower leaves directly from your device.
- **Disease Prediction**: Get predictions for common cauliflower diseases.
- **User-Friendly Interface**: Intuitive and visually appealing design.

## Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow/Keras
- **Deployment**: Localhost or cloud platform

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CauliCare.git
   
2.Navigate to the project directory:
cd CauliCare

3.Install dependencies:
pip install -r requirements.txt

4.Run the application:
python app.py

5.Open your browser and go to http://127.0.0.1:5000.


#Project Structure

CauliCare/
├── static/
│   ├── images/        # Background and other static images
│   └── css/           # CSS files
├── templates/
│   ├── index.html     # Upload page
│   └── result.html    # Prediction result page
├── app.py             # Flask application logic
├── model.h5           # Trained machine learning model
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

Future Enhancements
Add a database to store user uploads and predictions.
Deploy the application to a cloud service like AWS, Azure, or Heroku.
Expand to include predictions for other vegetable diseases.

