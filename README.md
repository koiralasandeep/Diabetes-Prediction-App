This is a Machine Learning web application built with Python that predicts whether a person is likely to have diabetes based on various health parameters. The project uses a trained ML model, a dataset from Kaggle, and a Streamlit-based frontend.

📂 Project Structure
bash
Copy
Edit
├── diabetes.csv              # Dataset used for training
├── Diabetes.ipynb           # Jupyter Notebook for model training and evaluation
├── trained_model.sav        # Serialized trained model using pickle
├── diabetes_app.py          # Streamlit app to deploy the model

🚀 How to Run the App Locally
Click Here: https://koiralasandeep-diabetes-prediction-app-diabetes-app-jjz8u5.streamlit.app/

🧠 Machine Learning Details
Dataset: Pima Indians Diabetes Database

Algorithm: Support Vector Machine

Features used:

Pregnancies
Glucose
BloodPressure
SkinThickness
Insulin
BMI
DiabetesPedigreeFunction
Age

📊 Output
The app takes user input for the features and returns a prediction:

"Diabetic"

"Non-Diabetic"

💾 Model File
The trained model is saved as trained_model.sav using the pickle library and loaded in the app.

🛠️ Dependencies
pandas
numpy
scikit-learn
streamlit
pickle
<img width="1920" alt="Screenshot 2025-05-18 at 11 46 09 AM" src="https://github.com/user-attachments/assets/bb3e2cef-7f19-47cc-b220-ec14079f73b1" />




