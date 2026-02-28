from flask import Flask, request, jsonify
import joblib
import numpy as np
import sqlite3

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# ------------------ PREDICT ROUTE ------------------

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    features = np.array([[
        data["Age"],
        data["SystolicBP"],
        data["DiastolicBP"],
        data["Blood glucose"],
        data["BodyTemp"],
        data["HeartRate"]
    ]])
    
    

    prediction_value = int(model.predict(features)[0])

    risk_mapping = {
        0: "Low Risk",
        1: "Mid Risk",
        2: "High Risk"
    }

    prediction = risk_mapping[prediction_value]
    probabilities = model.predict_proba(features)[0]
    confidence = float(max(probabilities))

    # Get most important feature
    feature_names = ["Age", "SystolicBP", "DiastolicBP", "Blood glucose", "BodyTemp", "HeartRate"]
    importances = model.feature_importances_
    top_feature = feature_names[np.argmax(importances)]

    return jsonify({
        "risk": prediction,
        "confidence": round(float(confidence), 2),
        "top_factor": top_feature
    })

# ------------------ EMERGENCY ROUTE ------------------

@app.route("/emergency", methods=["GET"])
def emergency():
    conn = sqlite3.connect("donors.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, blood_group, hemoglobin
        FROM donors
        WHERE hemoglobin > 12.5 AND available = 1
        LIMIT 5
    """)

    donors = cursor.fetchall()
    conn.close()

    donor_list = []
    for donor in donors:
        donor_list.append({
            "name": donor[0],
            "blood_group": donor[1],
            "hemoglobin": donor[2]
        })

    return jsonify(donor_list)

# ------------------

if __name__ == "__main__":
    app.run(debug=True)