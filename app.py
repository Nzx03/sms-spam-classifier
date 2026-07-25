import streamlit as st
import pickle
import os

st.title("SMS Spam Classifier")
st.caption("app.py loaded successfully ") 


with st.expander("Debug info (remove later)"):
    st.write("Working dir:", os.getcwd())
    st.write("Files here:", os.listdir("."))

try:
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))
    st.caption("Model & vectorizer loaded ")
except Exception as e:
    st.error(f"Error loading model/vectorizer: {e}")
    st.stop()

sms = st.text_area("Enter your message")

if st.button("Predict"):
    if not sms.strip():
        st.warning("Please enter a message first.")
    else:
        try:
            transformed_sms = vectorizer.transform([sms])
            prediction = model.predict(transformed_sms)

            if prediction[0] == 1:
                st.error("Spam 🚨")
            else:
                st.success("Not Spam ")
        except Exception as e:
            st.error(f"Prediction error: {e}")
