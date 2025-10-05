import streamlit as st
import joblib

# Load model
pipeline = joblib.load("models/sms_phish_pipeline.joblib")

st.title("📱 SMS Phishing Detector")
st.write("Enter an SMS message below to check if it's **ham** (safe) or **phish** (suspicious).")

message = st.text_area("Message:", "")

if st.button("Predict"):
    if message.strip():
        pred = pipeline.predict([message])[0]
        probs = pipeline.predict_proba([message])[0]
        st.write(f"**Prediction:** {pred}")
        st.write(f"**Probabilities:** Ham={probs[0]:.2f}, Phish={probs[1]:.2f}")
    else:
        st.warning("Please enter a message first.")
