# Insurance Charges Prediction App

This repository contains a Flask web application that predicts insurance charges based on user inputs such as age, sex, BMI, number of children, smoking status, and region. The application uses a Ridge Regression model for prediction.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)

## Overview

The Insurance Charges Prediction App is designed to provide an easy-to-use interface for predicting insurance charges. It utilizes a pre-trained Ridge Regression model and a Standard Scaler for preprocessing the input data. The model and scaler are loaded from serialized files using Python's `pickle` module.

## Installation

To get this project up and running on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/insurance-charges-prediction.git
    cd insurance-charges-prediction
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that the `Models` directory contains the `ridge.pkl` and `scaler (1).pkl` files.

5. Run the Flask application:
    ```bash
    python App.py
    ```

6. Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. On the home page, you will find a form where you can input the following details:
   - Age
   - Sex (0 for female, 1 for male)
   - BMI (Body Mass Index)
   - Children (Number of children)
   - Smoker (0 for non-smoker, 1 for smoker)
   - Region (0, 1, 2, or 3 representing different regions)

2. After filling out the form, submit it to receive the predicted insurance charges.

## File Descriptions

- `App.py`: The main Flask application file.
- `Models/`: Directory containing the serialized Ridge Regression model (`ridge.pkl`) and the Standard Scaler (`scaler (1).pkl`).
- `templates/index.html`: The HTML template for the home page.
- `templates/Home.html`: The HTML template for displaying the prediction result.
- `requirements.txt`: A list of Python dependencies required to run the application.

