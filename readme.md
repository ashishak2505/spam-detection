🔍 Project Overview

This project is an end-to-end NLP-based Spam Email Detection system that classifies email messages as Spam or Not Spam (Ham).
It uses classical NLP techniques, TF-IDF feature extraction, and a Logistic Regression classifier, deployed through an interactive Streamlit web application.

The goal is to build a reliable, interpretable, and deployable spam filter while handling real-world challenges like class imbalance.

🚀 Key Features

Text preprocessing using NLP techniques

TF-IDF vectorization with n-grams

Class imbalance handling using class weights

High recall-focused spam detection

Interactive web UI using Streamlit

Real-time prediction with confidence score

🧠 NLP & ML Pipeline
Raw Email Text
 → Text Cleaning & Preprocessing
 → TF-IDF Vectorization
 → Logistic Regression Classifier
 → Spam / Not Spam Prediction

🛠️ Tech Stack

Programming Language: Python

NLP: NLTK, Regex

Feature Engineering: TF-IDF (Scikit-learn)

Model: Logistic Regression (class_weight='balanced')

Deployment: Streamlit

Utilities: Joblib
📊 Dataset

UCI SMS Spam Collection Dataset

Labels:

0 → Ham (Not Spam)

1 → Spam

Dataset is imbalanced, making recall optimization critical.

📈 Model Performance
Metric	Spam Class
Precision	~91%
Recall	~92%
F1-score	~91%
Overall Accuracy	~98%

Why recall matters:
Missing spam emails is more costly than flagging a few legitimate ones.