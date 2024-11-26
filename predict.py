!pip install flask scikit-learn pandas

import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import OneHotEncoder
import pickle

app = Flask(__name__)

# Load the trained model and encoder
model = pickle.load(open('trained_model.pkl', 'rb'))  # Replace 'trained_model.pkl' with the actual filename
encoder = pickle.load(open('encoder.pkl', 'rb'))    # Replace 'encoder.pkl' with the actual filename

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict heart rate based on input features.
    """
    try:
        # Get the input data from the request
        data = request.get_json()

        # Create a DataFrame from the input data
        input_df = pd.DataFrame([data])

        # Preprocess the input data (similar to training)
        categorical_features = ['BMI Category', 'Sleep Disorder'] 
        numerical_features = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'Blood Pressure', 'Daily Steps']  

        # One-hot encode categorical features
        encoded_features = encoder.transform(input_df[['BMI Category']])  # Assuming 'BMI Category' is categorical
        encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['BMI Category']))
        input_df = input_df.drop('BMI Category', axis=1)  # Remove original categorical column
        input_df = pd.concat([input_df, encoded_df], axis=1)

        # --- Convert 'Blood Pressure' to numerical features (if needed) ---
        # Split 'Blood Pressure' into systolic and diastolic (if applicable)
        # Assuming Blood Pressure is in the format "Systolic/Diastolic"
        input_df[['Systolic', 'Diastolic']] = input_df['Blood Pressure'].str.split('/', expand=True).astype(float)
        
