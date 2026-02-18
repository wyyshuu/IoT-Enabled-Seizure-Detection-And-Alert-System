# How to Run in Google Colab

Since you want to run this on Google Colab, follow these steps.

1.  **Preparation**:
    -   Zip the entire `seizure` folder.
    -   Upload `seizure.zip` to your Google Drive or upload it directly to the Colab session.
    -   Unzip it in Colab:
        ```python
        !unzip seizure.zip
        %cd seizure
        ```

2.  **Install Dependencies**:
    Copy and paste this into a Colab cell:
    ```python
    !pip install flask pyngrok shap matplotlib scikit-learn
    ```

3.  **Setup Ngrok (Important)**:
    You need an Ngrok authtoken to expose the local Flask server to the internet.
    -   Go to [ngrok.com](https://dashboard.ngrok.com/get-started/your-authtoken) and sign up (it's free).
    -   Copy your Authtoken.
    -   Run this in Colab:
        ```python
        from pyngrok import ngrok
        ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN_HERE")
        ```

4.  **Run the App**:
    Run this code block in Colab to start the server:
    ```python
    from pyngrok import ngrok
    from app import app
    import threading

    # Open a tunnel to port 5000
    public_url = ngrok.connect(5000).public_url
    print(f" * Public URL: {public_url}")

    # Run Flask in a separate thread
    threading.Thread(target=app.run, kwargs={"port": 5000}).start()
    ```

5.  **Access the Dashboard**:
    Click the "Public URL" printed by the script (e.g., `http://xxxx-xx.ngrok-free.app`).

---
### Local Simulation
I have included a `create_mock_model.py` file. If you are testing this locally or want to see it work immediately without your specific trained model:
1.  Run `python create_mock_model.py` (this creates a dummy `model/seizure_model.pkl`).
2.  Run `python app.py`.
3.  Go to `http://127.0.0.1:5000`.
