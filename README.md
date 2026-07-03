# 🚀 GA-Optimized Income Prediction Flask API

A production-ready Flask REST API that serves predictions using a **Genetic Algorithm (GA) Optimized XGBoost model** trained on the Adult Income Census dataset.

The API predicts whether an individual's annual income is **greater than $50K** or **less than or equal to $50K** based on demographic and employment-related features.

---

# 🌐 Live API

**Base URL**

https://ga-optimized-income-prediction-flask-api.onrender.com

---

# 📌 Project Overview

This API is the deployment of my Machine Learning project:

**Evolutionary Feature Selection Using Genetic Algorithms for Optimizing Multiple Machine Learning Models**

The machine learning model was trained using:

- Adult Income Census Dataset
- Genetic Algorithm (PyGAD) for Feature Selection
- XGBoost Classifier
- Flask REST API
- Render Cloud Deployment

---

# ⚙️ Technologies Used

- Python
- Flask
- XGBoost
- Scikit-learn
- NumPy
- Pandas
- Joblib
- Gunicorn
- Render
- Git & GitHub

---

# 📂 Repository Structure

```text
GA-Optimized-Income-Prediction-Flask-API/
│
├── app.py
├── model.pkl
├── selected_features.pkl
├── label_encoders.pkl
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
```

---
# 🧪 API Testing

The API was successfully tested using **Postman**.

Tested Endpoints

- ✅ GET /
- ✅ GET /health
- ✅ POST /predict

---
# 🚀 API Endpoints Demonstration

## 🟢 Home

**GET /**


## ❤️ Health Check

**GET /health**


---

## 🤖 Predict Income

**POST /predict**

---

# 🧠 Model Information

**Algorithm**

- XGBoost Classifier

**Feature Selection**

- Genetic Algorithm (PyGAD)

**Selected Features**

- workclass
- education
- education_num
- occupation
- relationship
- race
- sex
- capital_gain
- capital_loss
- hours_per_week

---

# ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/RejuthaSree/GA-Optimized-Income-Prediction-Flask-API.git
```

Navigate into the project

```bash
cd GA-Optimized-Income-Prediction-Flask-API
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

or

```bash
flask run
```

---

# ☁️ Deployment

The API is deployed using **Render**.

Live URL

https://ga-optimized-income-prediction-flask-api.onrender.com

---

# 📚 Related Project

This API is the deployment version of the Machine Learning research project.

**Research Repository**

https://github.com/RejuthaSree/GA-Based-Feature-Selection-for-Income-Prediction

---

# 👩‍💻 Author

**Rejuthasree M**

---

# ⭐ Project Highlights

- ✅ End-to-End Machine Learning Deployment
- ✅ Genetic Algorithm Feature Selection
- ✅ GA-Optimized XGBoost Model
- ✅ REST API using Flask
- ✅ Cloud Deployment using Render
- ✅ API Testing with Postman

