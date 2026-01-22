from pydantic import BaseModel

class ChurnRequest(BaseModel):
    age: int
    monthly_charges: float
    tenure: int

class ChurnResponse(BaseModel):
    churn_probability: float
