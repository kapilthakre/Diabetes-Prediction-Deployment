# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Diabetes Predictor')
st.markdown("*A Machine Learning Web App, Built with Streamlit, Deployed using Heroku*")
st.write("")

# Taking input from user
Pregnancies = st.text_input("Number of Pregnancies eg. 0")
Glucose = st.text_input("Glucose (mg/dl)eg.80")
BloodPressure = st.text_input("Blood Pressure(mmHg)eg.80")
SkinThickness = st.text_input("Skin Thickness (mm) eg. 20")
Insulin = st.text_input("Insulin Level (IU/mL) eg. 80")
BMI = st.text_input("Body Mass Index (kg/m²) eg. 23.1")
DPF = st.text_input("Diabetes Pedigree Function eg. 0.52")
Age = st.text_input("Age (years) eg. 34")

# load model
model = pickle.load(open('diabetes_Prediction_model', 'rb'))

# Predictin function
def prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age):
    preg = int(Pregnancies)
    glu = float(Glucose)
    blp = float(BloodPressure)
    st = float(SkinThickness)
    insu = float(Insulin)
    bmi = float(BMI)
    dpf = float(DPF)
    age = int(Age)
    x = [[preg,glu,blp,st,insu,bmi,dpf,age]]
    return model.predict(x)[0]

# Submit button
if st.button('Submit'):
    result = prediction(Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age)
    if result==0:
        st.write("Great! You DON'T have Diabetes")
    else:
        st.write("Oops! You have Diabetes")
