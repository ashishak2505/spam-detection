import os

MODEL_PATH = "model/spam_classifier.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

print("Model file exists ✅")
