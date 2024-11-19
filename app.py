from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Set up logging for debug information
logging.basicConfig(level=logging.INFO)

# Load the model and scaler
model = joblib.load('diabetes_model.pkl')  # Load your model
scaler = joblib.load('scaler.pkl')         # Load your scaler

# Exact feature names as used during training and scaler fitting
feature_names = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
]

# Dictionary to store user inputs
user_inputs = {}

@app.route('/')
def home():
    return render_template('index.html', prediction=None, probability=None)

@app.route('/ask', methods=['POST'])
def ask():
    questions = [
        "Pregnancies (0-17): ",
        "Glucose (0-199): ",
        "Blood Pressure (0-122): ",
        "Skin Thickness (0-99): ",
        "Insulin (0-846): ",
        "BMI (0-67): ",
        "Diabetes Pedigree Function (0.078-2.42): ",
        "Age (21-81): "
    ]
    if len(user_inputs) < len(questions):
        return jsonify({"message": questions[len(user_inputs)]})
    else:
        return jsonify({"message": "All inputs collected. Ready for prediction!"})

@app.route('/input', methods=['POST'])
def input_value():
    data = request.json
    feature = data.get('feature')
    value = data.get('value')

    try:
        # Validate input
        if feature == "pregnancies":
            value = float(value)
            if not (0 <= value <= 17):
                raise ValueError("Pregnancies must be between 0 and 17.")
        elif feature == "glucose":
            value = float(value)
            if not (0 <= value <= 199):
                raise ValueError("Glucose must be between 0 and 199.")
        elif feature == "blood_pressure":
            value = float(value)
            if not (0 <= value <= 122):
                raise ValueError("Blood Pressure must be between 0 and 122.")
        elif feature == "skin_thickness":
            value = float(value)
            if not (0 <= value <= 99):
                raise ValueError("Skin Thickness must be between 0 and 99.")
        elif feature == "insulin":
            value = float(value)
            if not (0 <= value <= 846):
                raise ValueError("Insulin must be between 0 and 846.")
        elif feature == "bmi":
            value = float(value)
            if not (0 <= value <= 67):
                raise ValueError("BMI must be between 0 and 67.")
        elif feature == "diabetes_pedigree_function":
            value = float(value)
            if not (0.078 <= value <= 2.42):
                raise ValueError("Diabetes Pedigree Function must be between 0.078 and 2.42.")
        elif feature == "age":
            value = float(value)
            if not (21 <= value <= 81):
                raise ValueError("Age must be between 21 and 81.")
        else:
            raise ValueError("Invalid feature.")

        # Store the validated input
        user_inputs[feature] = value
        logging.info(f"Received input: {feature} = {value}")

        return jsonify({"message": f"Received {feature} = {value}. Thank you!"})

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({"message": str(ve)})
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred."})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure all necessary user inputs are present
        if len(user_inputs) < 8:
            return jsonify({"message": "Please provide all inputs before making a prediction."})

        # Gather all inputs for prediction
        data = [
            user_inputs.get('pregnancies', 0),
            user_inputs.get('glucose', 0),
            user_inputs.get('blood_pressure', 0),
            user_inputs.get('skin_thickness', 0),
            user_inputs.get('insulin', 0),
            user_inputs.get('bmi', 0),
            user_inputs.get('diabetes_pedigree_function', 0),
            user_inputs.get('age', 0)
        ]

        logging.info(f"Raw input data: {data}")

        # Convert to DataFrame
        data_df = pd.DataFrame([data], columns=feature_names)
        logging.info(f"DataFrame for scaling:\n{data_df}")

        # Scale the data
        data_scaled = scaler.transform(data_df)
        logging.info(f"Scaled input data: {data_scaled}")

        # Make prediction and get probability
        prediction = model.predict(data_scaled)
        probability = model.predict_proba(data_scaled)[0][1]  # Probability of having diabetes

        # Map prediction to "Diabetes" or "No Diabetes"
        prediction_text = "Diabetes" if prediction == 1 else "No Diabetes"
        logging.info(f"Prediction: {prediction_text}")
        logging.info(f"Probability of diabetes: {probability:.2f}")

        # Clear user inputs for the next session
        user_inputs.clear()

        return jsonify({"message": f"Prediction: {prediction_text}", "probability": round(probability, 2)})

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred. Please try again."})

@app.route('/restart', methods=['POST'])
def restart():
    global user_inputs
    user_inputs.clear()  # Clear previous inputs
    return jsonify({"message": "Session restarted. You can start entering data."})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
