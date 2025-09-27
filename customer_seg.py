import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("customer_scaler.pkl")

# Page config
st.set_page_config(page_title="Customer Segmentation Studio", page_icon="🧠", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🧠 Customer Segmentation Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict customer segments using K-Means clustering</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.header("📋 Input Customer Details")
age = st.sidebar.slider("Age", 18, 100, 35)
income = st.sidebar.number_input("Annual Income (₹)", min_value=0, max_value=200000, value=50000)
spending = st.sidebar.number_input("Total Spending (₹)", min_value=0, max_value=5000, value=1000)
store_purchases = st.sidebar.slider("Store Purchases", 0, 100, 10)
web_purchases = st.sidebar.slider("Web Purchases", 0, 100, 10)
web_visits = st.sidebar.slider("Monthly Website Visits", 0, 50, 3)
recency = st.sidebar.slider("Recency (days since last purchase)", 0, 365, 30)

# Input summary
with st.expander("📊 View Input Summary"):
    st.write(pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "Spending": [spending],
        "Store Purchases": [store_purchases],
        "Web Purchases": [web_purchases],
        "Web Visits": [web_visits],
        "Recency": [recency]
    }))

# Prepare data
input_data = pd.DataFrame({
    "age": [age],
    "Income": [income],
    "Total_spendding": [spending],
    "NumStorePurchases": [store_purchases],
    "NumWebPurchases": [web_purchases],
    "NumWebVisitsMonth": [web_visits],
    "Recency": [recency]
})
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("🚀 Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]
    st.success(f"🎯 Predicted Segment: *Cluster {cluster}*")

    # Optional interpretation
    st.markdown("---")
    st.subheader("🧠 Segment Insights")
    st.write(f"Cluster {cluster} might represent a group of customers with similar purchasing behavior. You can map this to marketing personas or loyalty tiers.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Built with ❤️ by Akash | Powered by Streamlit & scikit-learn</p>", unsafe_allow_html=True)