# Test Results

## Project Title

**Flood Prediction System Using Machine Learning**

---

# 1. Introduction

This document presents the results obtained after testing the Flood Prediction System. The application was tested to verify that all functional modules, including data input, machine learning prediction, result visualization, and user interface components, work as expected. Testing was performed using sample records from the flood dataset and various user input combinations.

---

# 2. Testing Environment

| Component                | Details                             |
| ------------------------ | ----------------------------------- |
| Operating System         | Windows 11                          |
| Programming Language     | Python 3.x                          |
| Framework                | Flask                               |
| Machine Learning Library | Scikit-learn                        |
| IDE                      | Visual Studio Code                  |
| Browser                  | Google Chrome                       |
| Dataset                  | Flood Dataset Classification (.csv) |

---

# 3. Test Execution Summary

| Test Category             | Status |
| ------------------------- | ------ |
| Application Launch        | Passed |
| Dataset Loading           | Passed |
| Model Loading             | Passed |
| User Input Validation     | Passed |
| Flood Prediction          | Passed |
| Risk Percentage Display   | Passed |
| Doughnut Chart Display    | Passed |
| Bar Chart Display         | Passed |
| Responsive User Interface | Passed |
| Background Animations     | Passed |

---

# 4. Observations

During testing, the following observations were made:

* The application launched successfully without runtime errors.
* The flood dataset was loaded correctly from the dataset directory.
* The trained machine learning model (`flood_model.pkl`) loaded successfully.
* The application accepted valid user inputs and prevented submission when required fields were empty.
* Flood prediction results were generated accurately based on the entered values.
* The calculated flood risk percentage was displayed correctly.
* Doughnut and bar charts were rendered successfully using Chart.js.
* The user interface remained responsive across different screen sizes.
* Background animations, including rain and moving waves, functioned correctly throughout testing.

---

# 5. Performance Evaluation

The application responded quickly to user requests and generated predictions within a short time. Dataset loading, model loading, and chart rendering were completed efficiently without noticeable delays. The overall performance was smooth during repeated testing.

---

# 6. Defects Found

During development, a few issues were identified and resolved:

| Issue                          | Resolution                                         |
| ------------------------------ | -------------------------------------------------- |
| Dataset file path not found    | Corrected the dataset path                         |
| Missing `flood_model.pkl` file | Trained the model and generated the file           |
| CSS syntax errors              | Corrected the stylesheet                           |
| Image loading issue            | Added images to the correct `static` folder        |
| Form field mismatches          | Updated field names to match the Flask application |

After applying these fixes, the application functioned as expected.

---

# 7. Overall Result

All planned functional and interface tests were executed successfully. The application performed reliably under normal operating conditions. No critical defects remained after testing.

**Total Test Cases Executed:** 15

**Passed:** 15

**Failed:** 0

**Success Rate:** 100%

---

# 8. Conclusion

The testing process confirmed that the Flood Prediction System meets the specified functional requirements. The machine learning model successfully predicts flood occurrences based on user-provided inputs, while the web application provides an interactive and user-friendly interface for displaying prediction results and visualizations. Based on the successful execution of all test cases, the system is considered stable, reliable, and ready for demonstration and project submission.
