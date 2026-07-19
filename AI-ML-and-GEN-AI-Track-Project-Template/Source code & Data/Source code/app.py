from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoder
model = joblib.load("flood_model.pkl")
encoder = joblib.load("label_encoder.pkl")


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

        # Read disaster type
        disaster_type = request.form["Disaster_Type"]

        # Try encoding if the encoder expects text labels
        try:
            disaster_type = encoder.transform([disaster_type])[0]
        except Exception:
            # Otherwise treat it as a numeric value
            disaster_type = int(disaster_type)

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

        # Feature names MUST match the training data
        input_data = pd.DataFrame([{
            "Disaster_Type": disaster_type,
            "Latitude": latitude,
            "Longitude": longitude,
            "Total_Deaths": total_deaths,
            "Total_Affected": total_affected,
            "duration": duration,
            "time": time,
            "Rainfall": rainfall,
            "Elevation": elevation,
            "Slope": slope,
            "distance": distance
        }])

        prediction = model.predict(input_data)[0]

        if hasattr(model, "predict_proba"):
            risk = int(model.predict_proba(input_data)[0][1] * 100)
        else:
            risk = 90 if prediction == 1 else 10

        result = "🌊 Flood Likely" if prediction == 1 else "✅ No Flood"

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
            prediction=f"Error: {str(e)}",
            rainfall=0,
            deaths=0,
            affected=0,
            risk=0
        )


if __name__ == "__main__":
    app.run(debug=True)