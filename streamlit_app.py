import streamlit as st
from src.predict import predict_quality

st.title("🍷 Wine Quality Prediction App")

st.markdown("Enter wine characteristics:")

# Feature inputs (11 total for this dataset)
features = {
    "Fixed Acidity": st.number_input("Fixed Acidity", 4.0, 16.0, 7.4),
    "Volatile Acidity": st.number_input("Volatile Acidity", 0.1, 2.0, 0.7),
    "Citric Acid": st.number_input("Citric Acid", 0.0, 1.0, 0.0),
    "Residual Sugar": st.number_input("Residual Sugar", 0.9, 15.0, 1.9),
    "Chlorides": st.number_input("Chlorides", 0.01, 0.2, 0.076),
    "Free Sulfur Dioxide": st.number_input("Free Sulfur Dioxide", 1.0, 72.0, 11.0),
    "Total Sulfur Dioxide": st.number_input("Total Sulfur Dioxide", 6.0, 300.0, 34.0),
    "Density": st.number_input("Density", 0.990, 1.005, 0.9978),
    "pH": st.number_input("pH", 2.5, 4.5, 3.51),
    "Sulphates": st.number_input("Sulphates", 0.2, 2.0, 0.56),
    "Alcohol": st.number_input("Alcohol", 8.0, 15.0, 9.4)
}

if st.button("Predict Quality"):
    input_values = list(features.values())
    result = predict_quality(input_values)
    st.success(f"Predicted Wine Quality: **{result}**")
