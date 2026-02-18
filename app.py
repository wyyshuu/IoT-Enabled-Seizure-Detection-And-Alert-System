from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os
import matplotlib
matplotlib.use('Agg') # Use Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
import io
import base64
import shap # Placeholder, will simulate if not fully installed or for speed
import random
from datetime import datetime

app = Flask(__name__)

# Load Model and Scaler
MODEL_PATH = 'model/seizure_model.pkl'
SCALER_PATH = 'model/scaler.pkl'

print("Loading model...")
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Model not found. Please run 'create_mock_model.py' first.")
    model = None
    scaler = None

# Risk mapping
RISK_MAP = {
    0: {'label': 'Low Risk', 'color': 'success', 'hex': '#28a745'},
    1: {'label': 'Moderate Risk', 'color': 'warning', 'hex': '#ffc107'},
    2: {'label': 'High Risk', 'color': 'danger', 'hex': '#dc3545'}
}

@app.route('/')
def home():
    return render_template('index.html', page='home')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_result = None
    
    if request.method == 'POST':
        try:
            # Gather inputs (assuming 5 demo inputs for simplicity in the UI, but model needs 178)
            # In a real scenario, we'd either input all, or load from file, or pad the rest.
            # Here for demo, we take 5 inputs and pad the rest with random/mean values.
            
            input_features = []
            features_names = ['X1', 'X2', 'X3', 'X4', 'X5']
            
            for name in features_names:
                val = request.form.get(name)
                input_features.append(float(val) if val else 0.0)
            
            # Pad with zeros or mean to match 178 features
            full_features = np.array(input_features + [0.0] * (178 - len(input_features))).reshape(1, -1)
            
            if scaler:
                full_features_scaled = scaler.transform(full_features)
            else:
                full_features_scaled = full_features # Fallback

            if model:
                # Predict
                prob = model.predict_proba(full_features_scaled)[0]
                pred_class = np.argmax(prob) # 0, 1, 2
                
                risk_info = RISK_MAP[pred_class]
                max_prob = prob[pred_class] * 100
                
                # AI Explanation Simulation
                if pred_class == 2:
                    explanation = "The AI model detects high-frequency chaotic signal patterns indicative of an impending seizure event. Immediate medical attention or precautionary measures are recommended."
                elif pred_class == 1:
                    explanation = "Moderate irregularities in EEG rhythm observed. The system recommends continued monitoring and patient precaution."
                else:
                    explanation = "EEG signals appear stable with normal rhythm. No immediate seizure risk detected."
                
                prediction_result = {
                    'class': risk_info['label'],
                    'probability': f"{max_prob:.2f}",
                    'color': risk_info['color'],
                    'explanation': explanation,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            
        except Exception as e:
            print(f"Error: {e}")
            prediction_result = {'error': str(e)}

    return render_template('predict.html', page='predict', result=prediction_result)

@app.route('/explainability')
def explainability():
    # Simulate SHAP plot
    img_str = generate_shap_plot_mock()
    return render_template('explainability.html', page='explainability', shap_plot=img_str)

@app.route('/history')
def history():
    # Mock Patient Data
    patient = {
        'id': 'PT-1024',
        'age': 29,
        'gender': 'Male',
        'medication': 'Carbamazepine 200mg',
        'history': [
            {'date': '2023-11-20', 'risk': 'High', 'prob': 88},
            {'date': '2023-11-21', 'risk': 'Low', 'prob': 12},
            {'date': '2023-11-22', 'risk': 'Moderate', 'prob': 56},
            {'date': '2023-11-23', 'risk': 'Low', 'prob': 10},
            {'date': '2023-11-24', 'risk': 'Low', 'prob': 15},
        ]
    }
    
    # Check if a search was performed (for demo mostly static)
    patient_id = request.args.get('patient_id')
    if patient_id:
        patient['id'] = patient_id # Just echo back for demo
        
    return render_template('history.html', page='history', patient=patient)

@app.route('/alerts')
def alerts():
    recent_alerts = [
        {'time': '10 min ago', 'message': 'High Risk detected for Patient PT-1024. Doctor notified.', 'type': 'danger'},
        {'time': '2 hours ago', 'message': 'Moderate Risk detected for Patient PT-1099.', 'type': 'warning'},
        {'time': '1 day ago', 'message': 'System Check: All sensors active.', 'type': 'info'}
    ]
    return render_template('alerts.html', page='alerts', alerts=recent_alerts)

@app.route('/simulate_alert', methods=['POST'])
def simulate_alert():
    # AJAX endpoint to simulate sending an alert
    return jsonify({'status': 'success', 'message': 'Emergency Alert Sent to Dr. Smith (555-0123)!'})

def generate_shap_plot_mock():
    # Generate a static bar chart to simulate SHAP feature importance
    features = [f'EEG_Feat_{i}' for i in range(1, 11)]
    importance = np.sort(np.random.rand(10))[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.barh(features[::-1], importance[::-1], color='#007bff')
    plt.xlabel('SHAP Feature Importance')
    plt.title('Top 10 EEG Features Contributing to Prediction')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img_str

if __name__ == '__main__':
    # When running locally
    app.run(debug=True)
