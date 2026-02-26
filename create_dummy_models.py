import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

# Create fake training data
X_dummy = np.random.rand(200, 4)

# Fake SoH between 50 and 100
y_soh_dummy = 50 + 50 * np.random.rand(200)

# Fake RUL between 100 and 1000 cycles
y_rul_dummy = 100 + 900 * np.random.rand(200)

# Train simple models
soh_model = LinearRegression()
soh_model.fit(X_dummy, y_soh_dummy)

rul_model = LinearRegression()
rul_model.fit(X_dummy, y_rul_dummy)

# Safety model (anomaly detection)
temp_data = np.random.rand(200, 1)
safety_model = IsolationForest(contamination=0.05)
safety_model.fit(temp_data)

# Save models
pickle.dump(soh_model, open("soh_model.pkl", "wb"))
pickle.dump(rul_model, open("rul_model.pkl", "wb"))
pickle.dump(safety_model, open("safety_model.pkl", "wb"))

print("Dummy models created successfully.")