from pydantic import BaseModel, Field
from typing import Literal

class VisaRequest(BaseModel):
    reading_score: float = Field(..., ge=0, le=9)
    listening_score: float = Field(..., ge=0, le=9)
    writing_score: float = Field(..., ge=0, le=9)
    speaking_score: float = Field(..., ge=0, le=9)

    age: int = Field(..., ge=18, le=60)
    gap_year: int = Field(..., ge=0, le=8)

    marital_status: Literal["single", "married", "divorced"]
    visa_type: Literal["STUDENT", "WORK", "DEPENDENT"]

class VisaResponse(BaseModel):
    success: bool
    prediction: str
    confidence: float
