import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#creating function for prediction
def diabetes_prediction(input_data):

    #changing input data to numpy arrays
    input_data_as_numpy_array = np.asarray(input_data)

    #Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The person is Non-Diabetic"
    else:
        return "The person is Diabetic"
    
    
def main():
    #title for webpage
    st.title('Diabetes Prediction App')
    
    #getiing input from user
    Pregnancies = st.text_input('Month of Pregnencies: ')
    Glucose = st.text_input('Glucose Level: ')
    BloodPressure = st.text_input('Level of BP: ')
    SkinThickness = st.text_input('Skin Thickness Value: ')
    Insulin = st.text_input('Insulin Level: ')
    BMI = st.text_input('BMI Value: ')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value: ')
    Age = st.text_input('Age: ')
    
    #prediction
    diagnosis = ''
    
    #button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
    
    
if __name__ =='__main__':
    main()
    