import requests
import streamlit as st
import pandas as pd
st.title("Loan Prediction App")
col1,col2=st.columns(2)

with col1:
    gender=st.radio("Select Gender:",('Male','Female'))

with col2:
    married=st.radio("Select Martial Status:",('Yes','No'))


ApplicantIncome=st.number_input("Enter Applicant Income:")
LoanAmount=st.number_input("Enter Loan Amount:")
Credit_History=st.number_input("Enter Credit History(0 or 1):")

if st.button("Predict"):
    # 4. Prepare data and predict
    payload = {
        "Gender": gender,
        "Married": married,
        "ApplicantIncome": ApplicantIncome,
        "LoanAmount": LoanAmount,
        "Credit_History": Credit_History
    }

    response=requests.post("http://127.0.0.1:5000/predict", json=payload)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Loan Status: {result['loan_approval_status']}")
    else:
        st.error("Error connecting to API")