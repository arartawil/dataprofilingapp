import streamlit as st
import pandas as pd
import numpy as np
import pickle

def app ():

    st.write("""
    # Pima Indian Diabetes Prediction App
    **Diabetes ** Type 2!
    """)

    st.sidebar.header('User Input Features')

    uploaded_file=None;
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
    else:
        def user_input_features():


            Glucose = st.sidebar.slider('Glucose', 0, 199, 100)
            BloodPressure = st.sidebar.slider('Blood Pressure', 0, 122, 50)
            BMI = st.sidebar.slider('Body Mass Index', 10.0 ,67.1 ,17.2)
            Age = st.sidebar.slider('Age', 10, 80, 60)
            data = {
                    'Glucose': Glucose,
                    'BloodPressure': BloodPressure,
                    'BMI': BMI,
                    'Age': Age,
            }
            features = pd.DataFrame(data, index=[0])
            return features
        input_df = user_input_features()

    st.subheader('User Input features')


    st.write(input_df)

    # Reads in saved classification model
    load_clf = pickle.load(open('Pima_clf.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(input_df)
    prediction_proba = load_clf.predict_proba(input_df)



    penguins_species = np.array(['Negative','Positive'])
    st.subheader('Your Result : ' +penguins_species[prediction][0])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)
