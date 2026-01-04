import streamlit as st
import joblib
import re
import os
import joblib
import nltk
from nltk.corpus import stopwords

import nltk
from nltk.corpus import stopwords

@st.cache_resource
def load_stopwords():
    try:
        return set(stopwords.words("english"))
    except LookupError:
        nltk.download("stopwords")
        return set(stopwords.words("english"))

stop_words = load_stopwords()



st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "spam_classifier.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)



stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    tokens = text.split()   # ✅ SAFE TOKENIZATION
    tokens = [w for w in tokens if w not in stop_words]

    return " ".join(tokens)


# ─── Sidebar ─────────────────────────────
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        """
        **Spam Email Detection App**
        
        Built using:
        - NLP preprocessing
        - TF-IDF Vectorization
        - Logistic Regression
        
        Designed for real-time spam detection.
        """
    )

# ─── Main UI ─────────────────────────────
st.title("📧 Spam Email Detection")
st.caption("Paste an email below to check whether it is spam.")

user_input = st.text_area(
    "Email Content",
    height=180,
    placeholder="Paste email text here..."
)

if st.button("🔍 Detect Spam"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter email text.")
    else:
        clean_text = preprocess_text(user_input)
        vector = tfidf.transform([clean_text])
        prediction = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0][1]

        st.markdown("---")

        if prediction == 1:
            st.error(f"🚨 **SPAM Email Detected**")
        else:
            st.success(f"✅ **This Email is NOT Spam**")

        st.metric(
            label="Spam Confidence",
            value=f"{prob*100:.2f}%"
        )
