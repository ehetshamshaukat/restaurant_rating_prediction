# 🍽️ Restaurant Rating Prediction: End-to-End MLOps Pipeline

## 📌 Project Overview

The **Restaurant Rating Prediction** system is a production-grade machine learning application designed to predict restaurant success metrics. By analyzing features such as **location, cost, cuisine type, and service availability**, the model generates data-driven predictions of restaurant ratings.

Unlike traditional notebook-based projects, this repository demonstrates a **complete MLOps lifecycle**, including:

- Modular architecture  
- Automated preprocessing pipelines  
- Multi-model benchmarking  
- Model serialization  
- Docker-based containerization  
- CI/CD deployment to AWS  

This project reflects industry-level engineering standards suitable for production environments.

---

## 🚀 Key Features

### 🔹 Modular Architecture
Decoupled components for:
- Data Ingestion  
- Data Transformation  
- Model Training  
- Prediction Pipeline  

Ensures scalability, maintainability, and production readiness.

---

### 🔹 Automated Model Selection
The training engine evaluates multiple algorithms, including:

- AdaBoost Regressor  
- Gradient Boosting Regressor  
- Random Forest Regressor  
- Linear Regression  

The model with the highest **R² Score (Coefficient of Determination)** is automatically selected and persisted.

---

### 🔹 Robust Preprocessing Pipeline
Built using **Scikit-Learn Pipelines** and **ColumnTransformer**:

- **Missing Value Imputation**
  - Median strategy (Numerical)
  - Most Frequent strategy (Categorical)

- **Feature Engineering**
  - Ordinal Encoding
  - Standard Scaling

All transformations are serialized for consistent inference in production.

---

### 🔹 Interactive Web Interface
Real-time predictions using a **Streamlit dashboard**.

---

### 🔹 Production-Ready Deployment
- Docker containerization  
- GitHub Actions CI/CD  
- Deployment to AWS EC2  
- Image storage in Amazon ECR  

---

## 📂 Project Structure

```bash
Restaurant_Rating_Prediction/
├── .github/workflows/              # CI/CD Pipeline (AWS ECR → EC2)
├── artifacts/                      # Processed data & serialized models
├── dataset/                        # Raw dataset
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # Train/Test split automation
│   │   ├── data_transformation.py  # Pipeline-based preprocessing
│   │   └── model_training.py       # Multi-model benchmarking
│   ├── pipeline/
│   │   └── prediction_pipeline.py  # Real-time inference logic
│   └── utils.py                    # Helper utilities
├── app.py                          # Streamlit application
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Project dependencies
└── setup.py                        # Package configuration
```

## 🏗️ The Engineering Pipelines📥 
### 🔹  1. Data Ingestion Pipeline
  1. The entry point of the system designed for data safety and reproducibility.Automated Splitting:
  2.  Performs a 75/25 Train-Test split using a fixed random_state to ensure scientific repeatability.
  3.  Artifact Management: Automatically generates a structured artifacts/ directory to decouple raw data from processed datasets.
  4.  Trigger Mechanism: Serves as the first link in the chain, passing file paths directly to the transformation layer.
### 🔹 2. Data Transformation Pipeline: (The Preprocessing Engine)
- Ensures raw restaurant data is converted into a mathematically optimized format.
- Numerical Stream: Handles missing values via Median Imputation and standardizes scales using StandardScaler.
- Categorical Stream: Uses Frequent Imputation for missing text and Ordinal Encoding to transform labels into numerical features.
- Serialization: Saves the fitted state into transformation.pkl to prevent Data Leakage and ensure consistent scaling during live inference.
### 🔹  3. Model Training Pipeline (The Competition Engine)
- A "Champion-Challenger" framework that finds the most accurate predictor.
- Multi-Model Benchmarking: Evaluates a suite of algorithms including Linear Regression, Random Forest, AdaBoost, and Gradient Boosting.
- Metric-Driven Selection: Automatically compares the $R^2$ Score of all models.
- Model Persistence: Promotes the "Best Model" and serializes it as model.pkl for production use.


## Image
<img width="1501" alt="Screenshot 2024-08-25 at 2 43 55 PM" src="https://github.com/user-attachments/assets/e1fc85cb-fa3e-4df7-8afd-a3c4679240c3">


