# Disease-Prediction-System-
# 🧠 Disease Prediction System

A Machine Learning web application built using **Streamlit** that predicts potential diseases based on 6 selected symptoms. The model is trained on a labeled dataset and uses a **Decision Tree Classifier** for predictions. This project includes:

- ✅ Login/Authentication
- ✅ PDF Export of Prediction Results
- ✅ Model Training Script
- ✅ Clean and Interactive Streamlit UI

---

## 🚀 Features

- Select exactly **6 symptoms** from a predefined list.
- Predict the **most likely disease** based on your symptoms.
- View the **confidence** score of the prediction.
- **Login authentication** for access control.
- Download your prediction result as a **PDF report**.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- FPDF (for PDF generation)
- Joblib (for model saving/loading)

---
---

## ⚙️ How to Run the Project

1. Clone the repository:
git clone https://github.com/Harsh-Rajoria/disease-prediction-system.git
cd disease-prediction-system
2. Install dependencies:
3. Train the model (optional if `disease_model.pkl` already exists):
4. Run the Streamlit app:
   streamlit run main.py
---

## 🔐 Default Login Credentials

You can log in using the following sample credentials:

- **Username:** admin
- **Password:** 1234

(You can modify or expand user credentials in `main.py`.)

---

## 📄 Sample Output

After selecting symptoms and clicking "Predict", the system displays the predicted disease and allows downloading the result as a PDF report.

---

