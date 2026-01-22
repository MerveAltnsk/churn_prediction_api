import numpy as np
from joblib import load

# Modeli yükle (uygulama başlarken bir kez)
model = load("app/ml/churn_model.pkl")

def predict_churn(age: int, monthly_charges: float, tenure: int) -> float:
    """
    Verilen müşteri bilgilerine göre churn olasılığı döner
    """
    features = np.array([[age, monthly_charges, tenure]])
    probability = model.predict_proba(features)[0][1]
    return float(probability)
