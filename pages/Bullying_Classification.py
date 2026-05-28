import joblib
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Bullying Classification")

# Use absolute paths based on script location
BASE_DIR = Path(__file__).parent.parent
VECTORIZER_PATH = BASE_DIR / 'tfidf_vectorizer.pkl'
MODEL_PATH = BASE_DIR / 'best_cyberbullying_model.pkl'

LABEL_MAP = {
    0: 'age',
    1: 'ethnicity',
    2: 'gender',
    3: 'not_cyberbullying',
    4: 'other_cyberbullying',
    5: 'religion',
}

st.title('Cyber Bullying Classification')


def load_vectorizer():
    if not VECTORIZER_PATH.exists():
        raise FileNotFoundError(f"Vectorizer file not found: {VECTORIZER_PATH.resolve()}")
    return joblib.load(VECTORIZER_PATH)


def load_classifier():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH.resolve()}")
    return joblib.load(MODEL_PATH)


vectorizer = load_vectorizer()
classifier = load_classifier()

text = st.text_input('Enter the text to classify')
if st.button('Classify'):
    if not text:
        st.warning('Please enter some text to classify.')
    else:
        vectorized = vectorizer.transform([text])
        result = classifier.predict(vectorized)
        predicted_value = result[0]
        try:
            predicted_index = int(predicted_value)
        except (TypeError, ValueError):
            predicted_index = None

        predicted_label = LABEL_MAP.get(predicted_index, str(predicted_value))
        st.success(f'The text is classified as: {predicted_label}')