# System Architecture Design

## Overview

The Flood Prediction System follows a machine learning-based architecture that combines data processing, model training, and a web-based prediction interface. The system collects environmental and geographical data, processes the information, applies machine learning algorithms, and generates flood risk predictions.

## Architecture Components

### 1. User Interface Layer

The user interacts with the system through a Flask-based web application. The interface allows users to enter environmental parameters required for prediction.

Input parameters include:
- Latitude
- Longitude
- Rainfall
- Elevation
- Slope
- Distance from water bodies
- Flood duration

### 2. Application Layer

The Flask application acts as a bridge between the user interface and the machine learning model.

Responsibilities:
- Receive user input
- Validate input data
- Send processed data to the ML model
- Display prediction results

### 3. Data Processing Layer

The input data is processed before prediction.

Processing steps:
- Data cleaning
- Handling missing values
- Feature selection
- Data transformation
- Normalization

### 4. Machine Learning Layer

The trained machine learning model analyzes input parameters and predicts flood risk.

Algorithms considered:
- Decision Tree
- Random Forest
- K-Nearest Neighbor (KNN)
- XGBoost

### 5. Output Layer

The final prediction is displayed to the user through the web interface.

Output:
- Flood risk level
- Prediction result
- Risk information


## System Architecture Flow

User
↓
Web Interface (Flask)
↓
Data Processing
↓
Machine Learning Model
↓
Flood Risk Prediction
↓
Display Result