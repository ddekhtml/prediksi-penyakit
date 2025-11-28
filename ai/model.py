import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

print("Model OK!")
MODEL_PATH = "model.pkl"
LABELS_PATH = "labels.pkl"

def train_model():
    print("Model OK! train")
    df = pd.read_csv("Training.csv")
    if "Unnamed: 133" in df.columns:
        df = df.drop(columns=["Unnamed: 133"])

    symptoms = df.columns[:-1]
    X = df[symptoms].astype(float)

    le = LabelEncoder()
    y = le.fit_transform(df["prognosis"])

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(le, LABELS_PATH)

    return "Model trained & saved!"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model belum dibuat! Jalankan train_model() dulu.")

    model = joblib.load(MODEL_PATH)
    labels = joblib.load(LABELS_PATH)

    return model, labels
