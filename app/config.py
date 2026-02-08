from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = "Visa Predictor API"
    VERSION = "1.0.0"
    ENV = os.getenv("ENV", "development")

settings = Settings()
