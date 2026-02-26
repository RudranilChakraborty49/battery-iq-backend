import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

soh_model = pickle.load(open(os.path.join(BASE_DIR, "models", "soh_model.pkl"), "rb"))
rul_model = pickle.load(open(os.path.join(BASE_DIR, "models", "rul_model.pkl"), "rb"))

def predict_soh(features):
    return float(soh_model.predict(features)[0])

def predict_rul(features):
    return int(rul_model.predict(features)[0])