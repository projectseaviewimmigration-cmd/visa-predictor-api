from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post(
        "/api/v1/predict",
        json={
            "age": 30,
            "country": "India",
            "education": "Masters",
            "experience": 5
        }
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
