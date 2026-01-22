import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump

# 1. Veriyi oku
data = pd.read_csv("data/churn.csv")

# 2. Feature (X) ve label (y) ayır
X = data[["age", "monthly_charges", "tenure"]]
y = data["churn"]

# 3. Modeli oluştur
model = LogisticRegression()

# 4. Modeli eğit
model.fit(X, y)

# 5. Modeli kaydet
dump(model, "app/ml/churn_model.pkl")

print("✅ Model trained and saved successfully")

