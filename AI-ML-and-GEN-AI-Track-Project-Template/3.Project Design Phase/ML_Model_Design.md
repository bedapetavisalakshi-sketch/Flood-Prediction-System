# Machine Learning Model Design

## Overview

The Flood Prediction System uses machine learning algorithms to identify patterns in historical flood data and predict future flood risks.

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Model Deployment


## Input Features

The model uses the following features:

- Rainfall
- Latitude
- Longitude
- Elevation
- Slope
- Distance from water bodies
- Flood duration


## Algorithms Used

### Decision Tree

Decision Tree creates a tree-based decision structure to classify flood risks based on input parameters.

### Random Forest

Random Forest combines multiple decision trees to improve prediction accuracy and reduce errors.

### K-Nearest Neighbor (KNN)

KNN predicts flood risk by comparing new data points with similar historical data.

### XGBoost

XGBoost is an advanced boosting algorithm that improves prediction performance by combining multiple weak models.


## Model Evaluation Metrics

The model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score