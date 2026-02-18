import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import os

# Create model directory
if not os.path.exists('model'):
    os.makedirs('model')

print("Generating mock EEG data...")

# Generate synthetic data mimicking EEG features
# 178 features (e.g., standard EEG dataset like UCI Epileptic Seizure Recognition)
# 5 classes usually, but here mapped to 3: High, Moderate, Low Risk
np.random.seed(42)
n_samples = 1000
n_features = 178

X = np.random.randn(n_samples, n_features)
# Generate target: 0 (Low), 1 (Moderate), 2 (High)
y = np.random.randint(0, 3, size=n_samples)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaler
print("Training Scaler...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Model
print("Training Random Forest Model...")
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Save
print("Saving model and scaler...")
with open('model/seizure_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('model/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Done! Mock model saved to 'model/' directory.")
