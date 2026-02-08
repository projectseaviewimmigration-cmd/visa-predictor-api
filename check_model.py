import joblib

model = joblib.load("model/model.joblib")

print("Model loaded successfully")
print("Model type:", type(model))
