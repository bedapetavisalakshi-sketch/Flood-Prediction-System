# Test Cases

## Project Title

**Flood Prediction System Using Machine Learning**

---

# Test Case Table

| Test ID | Test Case                     | Input                                     | Expected Result                                | Actual Result                     | Status |
| ------- | ----------------------------- | ----------------------------------------- | ---------------------------------------------- | --------------------------------- | ------ |
| TC-01   | Launch the Flask application  | Run `python app.py`                       | Application starts successfully without errors | Application started successfully  | Pass   |
| TC-02   | Open the dashboard            | Open `http://127.0.0.1:5000` in a browser | Flood Prediction Dashboard is displayed        | Dashboard displayed correctly     | Pass   |
| TC-03   | Load Machine Learning model   | Load `flood_model.pkl`                    | Model loads successfully                       | Model loaded successfully         | Pass   |
| TC-04   | Enter valid input values      | Valid disaster details                    | Prediction is generated                        | Prediction generated successfully | Pass   |
| TC-05   | Submit the prediction form    | Click **Predict Flood**                   | Prediction result is displayed                 | Prediction displayed correctly    | Pass   |
| TC-06   | Display flood risk percentage | Valid input values                        | Risk percentage is calculated and shown        | Risk percentage displayed         | Pass   |
| TC-07   | Display Doughnut Chart        | Prediction completed                      | Doughnut chart appears                         | Chart displayed successfully      | Pass   |
| TC-08   | Display Bar Chart             | Prediction completed                      | Bar chart appears                              | Chart displayed successfully      | Pass   |
| TC-09   | Leave a required field empty  | Missing rainfall value                    | Browser prevents form submission               | Validation message displayed      | Pass   |
| TC-10   | Enter decimal values          | Latitude, Longitude, Rainfall             | System accepts decimal values                  | Accepted successfully             | Pass   |
| TC-11   | Enter large numeric values    | Large rainfall or affected population     | System processes data correctly                | Prediction generated              | Pass   |
| TC-12   | Refresh the webpage           | Browser refresh                           | Dashboard reloads without errors               | Reloaded successfully             | Pass   |
| TC-13   | Check responsive layout       | Open on different screen sizes            | Interface adjusts properly                     | Responsive layout verified        | Pass   |
| TC-14   | Verify animations             | Open dashboard                            | Background, waves, and rain animations work    | Animations displayed correctly    | Pass   |
| TC-15   | Verify dataset loading        | Load `flood_dataset_classification.csv`   | Dataset loads successfully                     | Dataset loaded successfully       | Pass   |

---

# Summary

* **Total Test Cases:** 15
* **Passed:** 15
* **Failed:** 0
* **Overall Result:** **PASS**

---

# Conclusion

All planned test cases were executed successfully. The Flood Prediction System correctly loaded the dataset and trained model, accepted valid user inputs, generated flood predictions, displayed the calculated flood risk percentage, and visualized the results using charts. Input validation prevented incomplete form submissions, and the user interface remained responsive with all animations functioning correctly. Based on the executed test cases, the application meets the expected functional and performance requirements.
