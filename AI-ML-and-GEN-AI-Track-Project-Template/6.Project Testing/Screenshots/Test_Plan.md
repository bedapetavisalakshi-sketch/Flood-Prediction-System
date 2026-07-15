# Test Plan

## Project Title

**Flood Prediction System Using Machine Learning**

---

# 1. Introduction

The purpose of this test plan is to verify that the Flood Prediction System functions correctly and meets the intended project requirements. The application uses a Machine Learning model to predict the possibility of flood occurrence based on environmental and disaster-related parameters entered by the user. Testing is performed to ensure that all modules, including data input, prediction, visualization, and user interface, work accurately and efficiently.

---

# 2. Testing Objectives

The main objectives of testing are:

* To verify that the application starts without errors.
* To ensure that the dataset is loaded successfully.
* To validate that the trained machine learning model is loaded correctly.
* To verify that users can enter valid input values.
* To ensure that invalid or incomplete inputs are handled appropriately.
* To verify that flood predictions are generated correctly.
* To ensure that graphical visualizations such as charts are displayed correctly.
* To evaluate the overall performance and responsiveness of the web application.

---

# 3. Scope of Testing

The following modules are included in testing:

* User Interface (Dashboard)
* Input Form Validation
* Machine Learning Model Loading
* Prediction Module
* Result Display
* Risk Percentage Calculation
* Chart Visualization
* Overall Application Performance

---

# 4. Testing Environment

| Component                | Details                             |
| ------------------------ | ----------------------------------- |
| Operating System         | Windows 10 / Windows 11             |
| Programming Language     | Python 3.x                          |
| Framework                | Flask                               |
| Machine Learning Library | Scikit-learn                        |
| IDE                      | Visual Studio Code                  |
| Browser                  | Google Chrome / Microsoft Edge      |
| Dataset                  | Flood Dataset Classification (.csv) |

---

# 5. Testing Types

### Functional Testing

Checks whether each feature of the Flood Prediction System performs according to the specified requirements.

### User Interface Testing

Ensures that all pages, buttons, forms, labels, charts, and animations are displayed correctly.

### Input Validation Testing

Verifies that the system accepts valid inputs and prevents invalid or incomplete data from being submitted.

### Integration Testing

Confirms that all components including the dataset, machine learning model, Flask backend, HTML templates, CSS styling, and charts work together successfully.

### Performance Testing

Evaluates whether the application responds quickly and remains stable during prediction and visualization.

---

# 6. Test Strategy

Testing is performed using sample records from the flood dataset. Different combinations of rainfall, deaths, affected population, elevation, slope, and other parameters are entered into the application. The prediction results are verified and compared with expected outputs. The charts and dashboard interface are also checked for correct visualization.

---

# 7. Test Deliverables

The following documents are prepared during testing:

* Test Plan
* Test Cases
* Test Results
* Bug Report
* Application Screenshots (if available)

---

# 8. Entry Criteria

Testing begins after:

* Dataset has been added successfully.
* Machine learning model has been trained.
* `flood_model.pkl` has been generated.
* Flask application runs successfully.
* All required libraries are installed.

---

# 9. Exit Criteria

Testing is considered complete when:

* All major functionalities execute successfully.
* Prediction results are generated correctly.
* Charts are displayed without errors.
* No critical defects remain unresolved.
* The application operates reliably under normal usage conditions.

---

# 10. Conclusion

The Test Plan provides a structured approach for validating the Flood Prediction System. By testing the application's functionality, user interface, prediction accuracy, and overall performance, the system can be evaluated for reliability and readiness for deployment. Successful completion of testing confirms that the application meets the project objectives and delivers accurate flood prediction results through an easy-to-use web interface.
