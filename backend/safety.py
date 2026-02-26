import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

safety_model = pickle.load(open(os.path.join(BASE_DIR, "models", "safety_model.pkl"), "rb"))

def check_safety(temp_rise_rate):
    
    result = safety_model.predict([[temp_rise_rate]])
    
    if result[0] == -1:
        return "CRITICAL"
    elif temp_rise_rate > 1.5:
        return "WARNING"
    else:
        return "SAFE"