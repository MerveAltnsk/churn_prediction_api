from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from app.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    monthly_charges = Column(Float, nullable=False)
    tenure = Column(Integer, nullable=False)
    churn_probability = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
