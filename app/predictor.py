import joblib
import pandas as pd

_model = None

def load_model():
    global _model
    _model = joblib.load("model/model.joblib")

def predict_visa(data):
    if _model is None:
        raise RuntimeError("Model not loaded")

    df = pd.DataFrame([data.dict()])
    proba = _model.predict_proba(df)[0]
    approved_prob = proba[1]

    prediction = "Approved" if approved_prob >= 0.5 else "Rejected"
    confidence = round(approved_prob * 100, 2)

    return prediction, confidence
