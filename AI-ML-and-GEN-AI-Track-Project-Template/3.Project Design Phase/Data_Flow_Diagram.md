# Data Flow Design

## Overview

The data flow describes how data moves through different components of the Flood Prediction System.

## Data Flow Steps

### Step 1: Data Collection

Historical flood datasets are collected from reliable sources. The dataset contains environmental and geographical information related to previous flood events.

### Step 2: Data Preprocessing

The collected data is cleaned and prepared for machine learning.

Operations include:
- Removing unwanted data
- Handling missing values
- Converting data formats
- Selecting important features

### Step 3: Model Training

The processed dataset is divided into training and testing data.

Training data is used to train machine learning algorithms, while testing data is used to evaluate performance.

### Step 4: Prediction

New user input data is provided to the trained model.

The model analyzes the input and predicts the flood risk.

### Step 5: Result Display

The prediction result is displayed through the Flask web application.


## Data Flow Diagram

Dataset
↓
Data Preprocessing
↓
Feature Extraction
↓
ML Model Training
↓
Trained Model
↓
User Input
↓
Prediction
↓
Flood Risk Result