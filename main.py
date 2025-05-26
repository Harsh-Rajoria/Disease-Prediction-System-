import pandas as pd
import streamlit as st
import joblib
from fpdf import FPDF
import os

# --- LOGIN AUTHENTICATION ---
users = {"admin": "1234", "doctor": "abcd"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login to Use the Disease Predictor")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if users.get(username) == password:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")
    st.stop()

# --- MAIN PAGE ---
st.title("🧠 Disease Prediction System")
st.markdown("Welcome! Select 6 symptoms to predict the possible disease.")

# Load model and data
model = joblib.load("disease_model.pkl")
df = pd.read_csv("train_data.csv")
symptom_columns = df.columns.drop("disease")

# Show dataset (optional)
with st.expander("🔍 View Sample Dataset"):
    st.dataframe(df.head())

# Show diseases
st.subheader("🦠 Diseases in the Dataset:")
diseases = df["disease"].unique()
cols = st.columns(5)
for i, disease in enumerate(diseases):
    cols[i % 5].write(f"✅ {disease}")

# SYMPTOM SELECTION
selected_symptoms = st.multiselect("Select Exactly 6 Symptoms", symptom_columns.tolist(), max_selections=6)
if len(selected_symptoms) < 6:
    st.warning("Please select exactly 6 symptoms.")
elif len(selected_symptoms) > 6:
    st.error("You can only select 6 symptoms.")
else:
    st.success("Selected Symptoms:")
    st.write(", ".join(selected_symptoms))

    # Prepare input vector
    input_vector = [1 if col in selected_symptoms else 0 for col in symptom_columns]
    prediction = model.predict([input_vector])[0]
    probability = model.predict_proba([input_vector]).max()

    # PREDICT
    if st.button("🔍 Predict Disease"):
        st.subheader("🩺 Prediction Result:")
        st.write(f"**Predicted Disease:** {prediction}")
        st.write(f"**Confidence:** {probability:.2%}")

        # PDF Export
        if st.button("📄 Download PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Disease Prediction Report", ln=True, align="C")
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"Predicted Disease: {prediction}", ln=True)
            pdf.cell(200, 10, txt=f"Confidence: {probability:.2%}", ln=True)
            pdf.ln(5)
            pdf.cell(200, 10, txt="Selected Symptoms:", ln=True)
            for sym in selected_symptoms:
                pdf.cell(200, 10, txt=f"- {sym}", ln=True)

            pdf.output("disease_report.pdf")
            with open("disease_report.pdf", "rb") as f:
                st.download_button("⬇️ Download Report", f, file_name="disease_report.pdf")
