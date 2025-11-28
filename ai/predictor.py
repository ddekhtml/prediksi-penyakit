# ai/predictor.py
import os
import joblib
import numpy as np
import pandas as pd
from django.conf import settings

# Load model
model_path = os.path.join(settings.BASE_DIR, "ai", "model.joblib")
model = joblib.load(model_path)

# Load dataset (untuk urutan gejala dan nama penyakit)
df = pd.read_csv(os.path.join(settings.BASE_DIR, "static", "Training.csv"))
symptom_columns = df.drop(columns=["prognosis"]).columns.tolist()

# Mapping label numerik → nama penyakit
disease_names = df["prognosis"].unique().tolist()
DISEASE_MAPPING = {i: name for i, name in enumerate(disease_names)}

def predict(symptoms_data):
    """
    symptoms_data = dict { 'headache': 1, 'itching': 0, ... }
    Return: nama penyakit
    """
    values = [symptoms_data.get(col, 0) for col in symptom_columns]
    data = np.array(values).reshape(1, -1)

    predicted_label = model.predict(data)[0]
    predicted_name = DISEASE_MAPPING[predicted_label]

    return predicted_name
