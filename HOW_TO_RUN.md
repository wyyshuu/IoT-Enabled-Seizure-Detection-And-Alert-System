# How to Run Locally

You can run the seizure prediction dashboard on your local machine using these commands.

### 1. Open Terminal (PowerShell or Command Prompt)
Navigate to the project folder:
```powershell
cd c:\Users\Home\Desktop\seizure
```

### 2. Activate Virtual Environment & Run
Since we set up a virtual environment, use this command to start the app:
```powershell
.\venv\Scripts\python app.py
```

### 3. View the Dashboard
Once the app is running, open your web browser and go to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---
**Note:**
If you need to install dependencies manually again (e.g., if you deleted the venv), run:
```powershell
.\venv\Scripts\pip install flask numpy pandas scikit-learn matplotlib shap
```
