# DiabetesGPT: An Interactive Diabetes Prediction Tool

![DiabetesGPT Home Page](https://i.imgur.com/5lFeTM5.png)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [User Inputs](#user-inputs)
- [SDG Addressed](#sdg-addressed)

## Project Overview
DiabetesGPT is a web-based application designed to assess an individual's risk of developing diabetes based on critical health metrics. The application utilizes a conversational bot interface to guide users through a series of questions regarding their health, providing personalized feedback and recommendations based on the input data.

## Features
- **Interactive Chat Interface:** Engage with the bot in a conversational format.
- **User-Friendly Design:** Simple and intuitive input process.
- **Real-time Predictions:** Get immediate feedback on diabetes risk based on user inputs.
- **Health Awareness:** Educate users about diabetes risk factors and encourage preventive measures.

## Technologies Used
- **Flask:** For building the web application.
- **HTML/CSS:** For frontend design and styling.
- **JavaScript:** For handling user interactions and API calls.
- **Machine Learning:** Utilizes algorithms trained on the Pima Indians Diabetes dataset for predictions.

## Getting Started
To run the DiabetesGPT application locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GauravSrivastava-prog/Assignment-1
   cd Assignment-1/Documents/'My Computer'/SEM-3/AI-ML/Diabetes-Model
   ```

2. **Create a Virtual Environment:
   ```bash
     python -m venv venv
     source venv/bin/activate  # On macOS/Linux
     venv\Scripts\activate     # On Windows
   ```

3. **Run the Application:
   ```bash
   python app.py
   ```

**Navigate to http://127.0.0.1:5001 in your web browser to access the application.

## User Inputs

The application requires the following inputs from the user to assess diabetes risk:

- Number of pregnancies
- Glucose level
- Blood pressure
- Skin thickness
- Insulin level
- Body mass index (BMI)
- Diabetes pedigree function
- Age

## SDG Addressed

This project addresses Goal 3: Good Health and Well-being from the United Nations Sustainable Development Goals (SDGs). By providing a tool to assess diabetes risk, it promotes awareness and preventive health measures, contributing to better health outcomes for individuals.
