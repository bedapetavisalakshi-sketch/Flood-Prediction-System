
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load Model
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

        disaster_type = int(request.form.get("Disaster_Type", 0))
        latitude = float(request.form.get("Latitude", 0))
        longitude = float(request.form.get("Longitude", 0))
        total_deaths = float(request.form.get("Total_Deaths", 0))
        total_affected = float(request.form.get("Total_Affected", 0))
        duration = float(request.form.get("duration", 0))
        time = float(request.form.get("time", 0))
        rainfall = float(request.form.get("Rainfall", 0))
        elevation = float(request.form.get("Elevation", 0))
        slope = float(request.form.get("Slope", 0))
        distance = float(request.form.get("distance", 0))

        df = pd.DataFrame([{
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

        prediction = model.predict(df)[0]

        if hasattr(model, "predict_proba"):
            risk = int(model.predict_proba(df)[0][1] * 100)
        else:
            risk = 85 if prediction == 1 else 15

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
            prediction="Error: " + str(e),
            rainfall=0,
            deaths=0,
            affected=0,
            risk=0
        )


if __name__ == "__main__":
    app.run(debug=True)