from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and required files
model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
selected_features = joblib.load("selected_features.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Income Prediction API is Running ",
        "model": "GA-Optimized XGBoost",
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if data is None:
            return jsonify({
                "status": "error",
                "message": "No JSON data received."
            }), 400

        # Convert JSON to DataFrame
        df = pd.DataFrame([data])

        # Encode categorical columns
        categorical_cols = [
            "workclass",
            "education",
            "occupation",
            "relationship",
            "race",
            "sex"
        ]

        for col in categorical_cols:
            df[col] = label_encoders[col].transform(df[col])

        # Arrange features in correct order
        df = df[selected_features]

        # Prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0].max()

        income = ">50K" if prediction == 1 else "<=50K"

        return jsonify({
            "status": "success",
            "model": "GA-Optimized XGBoost",
            "prediction": income,
            "confidence": f"{probability*100:.2f}%"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)