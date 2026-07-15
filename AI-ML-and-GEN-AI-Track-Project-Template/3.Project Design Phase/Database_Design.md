# Database Design

## Overview

The Flood Prediction System mainly uses datasets for storing historical flood information and environmental parameters.

## Dataset Structure

The dataset contains the following attributes:

| Attribute | Description |
|-----------|-------------|
| Latitude | Location coordinate |
| Longitude | Location coordinate |
| Rainfall | Amount of rainfall |
| Elevation | Height above sea level |
| Slope | Land surface inclination |
| Distance | Distance from water source |
| Duration | Flood duration |
| Risk Level | Flood prediction output |


## Data Storage

The system stores:

- Historical flood records
- Training data
- Testing data
- Prediction results

The dataset is used for training and improving the machine learning model.