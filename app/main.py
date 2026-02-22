from fastapi import FastAPI
from app.schemas import VisaRequest, VisaResponse
from app.predictor import load_model, predict_visa

app = FastAPI(title="Visa Predictor API", version="1.0.0")

@app.on_event("startup")
def startup():
    load_model()

@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {"status": "ok"}


@app.post("/api/v1/predict", response_model=VisaResponse)
def predict(data: VisaRequest):
    prediction, confidence = predict_visa(data)
    return {
        "success": True,
        "prediction": prediction,
        "confidence": confidence
    }
