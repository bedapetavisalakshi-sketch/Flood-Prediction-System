# Bug Report

## Project Title

**Flood Prediction System Using Machine Learning**

---

# 1. Introduction

This document records the issues identified during the development and testing of the Flood Prediction System. Each bug was analyzed, corrected, and verified to ensure the stability and reliability of the application. The report serves as evidence of the debugging process and confirms that all major issues encountered during implementation were resolved successfully.

---

# 2. Bug Summary

| Bug ID | Module            | Description                                                            | Cause                                                      | Resolution                                                                   | Status |
| ------ | ----------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------- | ------ |
| BUG-01 | Dataset Loading   | Dataset file could not be found during model training.                 | Incorrect dataset path specified in the code.              | Updated the correct dataset path and verified successful loading.            | Fixed  |
| BUG-02 | Model Loading     | `flood_model.pkl` file was missing when running the Flask application. | Machine learning model had not been trained.               | Trained the model using `train_model.py` and generated `flood_model.pkl`.    | Fixed  |
| BUG-03 | Flask Application | Application failed to display prediction results.                      | Incorrect form field mapping between HTML and Flask.       | Updated input field names to match the Flask backend.                        | Fixed  |
| BUG-04 | CSS Styling       | CSS syntax errors caused the dashboard layout to break.                | Incorrect placement of animation and selector blocks.      | Corrected the CSS syntax and verified the layout.                            | Fixed  |
| BUG-05 | Image Loading     | Flood and cloud images were not displayed.                             | Images were missing or placed outside the `static` folder. | Moved image files to the correct `static` directory.                         | Fixed  |
| BUG-06 | Chart Display     | Charts were not visible after prediction.                              | Prediction values were not passed correctly to Chart.js.   | Corrected data binding between Flask and the HTML template.                  | Fixed  |
| BUG-07 | Input Validation  | Invalid or incomplete form submissions caused errors.                  | Required input validation was missing.                     | Added HTML validation using the `required` attribute and proper input types. | Fixed  |
| BUG-08 | UI Responsiveness | Dashboard layout was not properly aligned on smaller screens.          | Missing responsive CSS adjustments.                        | Added responsive CSS rules using media queries.                              | Fixed  |

---

# 3. Bug Resolution Process

The development process involved identifying bugs through continuous testing and debugging. Errors related to dataset loading, model generation, HTML form handling, CSS styling, and image rendering were corrected. Each issue was re-tested after applying the fix to ensure that it no longer affected the application's functionality.

---

# 4. Final Status

After resolving all identified issues:

* Dataset loads successfully.
* Machine learning model loads without errors.
* Prediction is generated correctly.
* Dashboard interface displays properly.
* Charts render successfully.
* Images and animations load correctly.
* User input validation functions as expected.
* The application runs smoothly without critical defects.

---

# 5. Conclusion

All major bugs identified during the development and testing phases were successfully resolved. The Flood Prediction System now operates as expected, providing reliable flood predictions through a user-friendly web interface. Final verification confirmed that no critical or high-priority defects remain, and the application is stable and ready for project demonstration and deployment.
