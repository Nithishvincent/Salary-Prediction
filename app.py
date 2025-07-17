# app.py
import streamlit as st
import joblib

model = joblib.load("salary_model.pkl")

st.title("Employee Salary Predictor")

experience = st.slider("Years of Experience", 0, 30)
education_level = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"])
age = st.number_input("Age", min_value=18, max_value=65)

# Dummy encoding or map to numeric if needed
education_map = {"Bachelors": 0, "Masters": 1, "PhD": 2}
education_num = education_map[education_level]

features = [[experience, education_num, age]]

if st.button("Predict Salary"):
    salary = model.predict(features)
    st.success(f"Estimated Salary: ₹{salary[0]:,.2f}")
