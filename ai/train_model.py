import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from django.conf import settings

# Load dataset
file_path = os.path.join(settings.BASE_DIR, "static", "Training.csv")
df = pd.read_csv(file_path)

# Preprocessing model
X = df.drop(columns=["prognosis"])
y = LabelEncoder().fit_transform(df["prognosis"])

model = RandomForestClassifier()
model.fit(X, y)

# Save model
model_path = os.path.join(settings.BASE_DIR, "ai", "model.joblib")
joblib.dump(model, model_path)

print("🎉 MODEL BERHASIL DISIMPAN:", model_path)
