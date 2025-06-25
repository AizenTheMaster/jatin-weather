# salary_app.py 💼 Fixed for 10 inputs by Himan

import streamlit as st
import numpy as np
import pickle

# Load XGBoost model directly
with open('placement.sav', "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.set_page_config(page_title="💼 Salary Predictor by Himanshu", layout="centered")
st.title("💼 Salary Prediction App - By Himanshu")

st.markdown("Fill the student/professional profile to predict **expected salary** (XGBoost, 10 features).")

# Input fields (split across columns for better layout)
col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input("📚 CGPA", step=0.01)
    iq = st.number_input("🧠 IQ Level")
    age = st.number_input("🎂 Age")
    experience = st.number_input("👔 Years of Experience")
    english_score = st.number_input("🗣️ English Test Score")

with col2:
    skill_score = st.number_input("💡 Skill Score")
    projects = st.number_input("💼 Number of Projects")
    grad_year = st.number_input("🎓 Graduation Year")
    city_tier = st.selectbox("🏙️ City Tier", [1, 2, 3])
    domain_score = st.number_input("📊 Domain Knowledge Score")

# Final input array — match exact order of model training
input_data = np.array([[cgpa, iq, age, experience, skill_score, projects,
                        english_score, grad_year, city_tier, domain_score]])

# Predict
if st.button("💸 Predict Salary"):
    salary = model.predict(input_data)[0]
    st.success(f"💰 Predicted Salary: ₹{salary:,.2f}")
