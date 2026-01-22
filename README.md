# Churn Prediction API

A production-style backend service that provides customer churn predictions using a machine learning model, FastAPI, and PostgreSQL.

## 🚀 Tech Stack
- Python 3
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy
- scikit-learn
- Pandas

## 📌 Features
- Train a churn prediction ML model
- REST API for predictions
- PostgreSQL persistence with transactions
- Prediction history endpoint

## ML Model
- Logistic Regression
- Features: age, monthly_charges, tenure

## ▶️ How to Run

### 1. Start PostgreSQL
```bash
docker run --name churn-postgres \
  -e POSTGRES_USER=churn_user \
  -e POSTGRES_PASSWORD=churn_pass \
  -e POSTGRES_DB=churn_db \
  -p 5432:5432 \
  -d postgres:15
```

### 2. Install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Train model
```bash
python app/ml/train.py
```

### 4. Run API
```bash
uvicorn app.main:app --reload
```

### 5. API Docs

Open: http://127.0.0.1:8000/docs

## Endpoints

POST /predict – Get churn probability

GET /predictions – List past predictions

