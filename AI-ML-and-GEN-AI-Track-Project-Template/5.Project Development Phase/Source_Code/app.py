from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained Machine Learning model
model = joblib.load("flood_model.pkl")


@app.route("/")
def home():
    return render_template(
        "index.html",
        prediction="",
        rainfall=0,
        deaths=0,
        affected=0,
        risk=0
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:

        # Get input values from HTML form
        disaster_type = int(request.form["Disaster_Type"])
        latitude = float(request.form["Latitude"])
        longitude = float(request.form["Longitude"])
        total_deaths = float(request.form["Total_Deaths"])
        total_affected = float(request.form["Total_Affected"])
        duration = float(request.form["duration"])
        time = float(request.form["time"])
        rainfall = float(request.form["Rainfall"])
        elevation = float(request.form["Elevation"])
        slope = float(request.form["Slope"])
        distance = float(request.form["distance"])

        # Create DataFrame
        input_data = pd.DataFrame([{
            "Disaster Type": disaster_type,
            "Latitude": latitude,
            "Longitude": longitude,
            "Total Deaths": total_deaths,
            "Total Affected": total_affected,
            "duration": duration,
            "time": time,
            "Rainfall": rainfall,
            "Elevation": elevation,
            "Slope": slope,
            "distance": distance
        }])

        # Prediction
        prediction = int(model.predict(input_data)[0])

        # Risk Percentage
        if hasattr(model, "predict_proba"):
            risk = round(model.predict_proba(input_data)[0][1] * 100, 2)
        else:
            risk = 90 if prediction == 1 else 10

        # Prediction Message
        if prediction == 1:
            result = "🌊 Flood Likely"
        else:
            result = "✅ No Flood"

        return render_template(
            "index.html",
            prediction=result,
            rainfall=rainfall,
            deaths=total_deaths,
            affected=total_affected,
            risk=risk
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction="❌ Error occurred",
            rainfall=0,
            deaths=0,
            affected=0,
            risk=0,
            error=str(e)
        )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )