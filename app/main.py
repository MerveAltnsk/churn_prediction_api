from fastapi import FastAPI
from app.schemas import ChurnRequest, ChurnResponse
from app.ml.predict import predict_churn
from app.database import engine
from app import models
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.models import Prediction
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Bu satır:
# tüm modelleri tarar
# yoksa tabloları oluşturur
# varsa dokunmaz (safe)


@app.get("/")
def root():
    return {"message": "Churn Prediction API is running 🚀"}

@app.post("/predict", response_model=ChurnResponse)
def predict(request: ChurnRequest, db: Session = Depends(get_db)):
    probability = predict_churn(
        age=request.age,
        monthly_charges=request.monthly_charges,
        tenure=request.tenure
    )

    prediction = Prediction(
        age=request.age,
        monthly_charges=request.monthly_charges,
        tenure=request.tenure,
        churn_probability=probability
    )

    db.add(prediction)
    db.commit()    # Commit olmazsa → DB’ye gitmez
    db.refresh(prediction)   # DB’nin ürettiği id, created_at gibi alanları geri alır

    return {"churn_probability": probability}


# Veritabanına kaydedilen tahminleri API üzerinden okuruz.
@app.get("/predictions", response_model=List[ChurnResponse])
def get_predictions(db: Session = Depends(get_db)):
    predictions = db.query(Prediction).all() # tüm kayıtları alır
    return [
        {"churn_probability": p.churn_probability}
        for p in predictions
    ]
