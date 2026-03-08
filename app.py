import streamlit as st
import pickle
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences

# Page config
st.set_page_config(
    page_title="Movie Sentiment Analyzer",
    page_icon="🎬"
)

# Load model
@st.cache_resource
def load_model():
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    model = tf.keras.models.load_model("model.h5")
    return tokenizer, model


tokenizer, model = load_model()

# Title
st.title("🎬 Movie Review Sentiment Analyzer")

st.write("This application allows you to analyze movie reviews and predict whether they express positive or negative sentiment. Powered by a deep learning model trained on the IMDB dataset using LSTM, it provides accurate sentiment predictions with confidence scores.")

st.markdown("""
    ### How to Use This Application
    - Type or paste a movie review in the text area.
    - Click "Analyze Sentiment" to get the prediction.
    - Receive instant predictions with sentiment (Positive/Negative) and confidence levels.
    - Try example reviews to see the model in action.
    """)
    
# Session state for review text
if "review_text" not in st.session_state:
    st.session_state.review_text = ""

# Text input
review = st.text_area(
    "Write your review here:",
    value=st.session_state.review_text,
    key="review_box"
)

# Prediction function
def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=200)

    prediction = model.predict(padded)

    sentiment = "Positive 😊" if prediction[0][0] > 0.5 else "Negative 😔"
    confidence = prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0]

    return sentiment, confidence


# Predict button
if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        sentiment, confidence = predict_sentiment(review)

        st.subheader("Prediction Result")

        if "Positive" in sentiment:
            st.success(sentiment)
        else:
            st.error(sentiment)

        st.write(f"Confidence: **{confidence:.2%}**")


# Example reviews section
st.markdown("---")
st.subheader("Try Example Reviews")

example_reviews = [
    "This movie was absolutely fantastic! The acting and story were amazing.",
    "Terrible movie. I wasted my time watching it.",
    "The movie was okay, not great but not bad either."
]

col1, col2, col3 = st.columns(3)

if col1.button("Example 1"):
    st.session_state.review_text = example_reviews[0]
    st.rerun()

if col2.button("Example 2"):
    st.session_state.review_text = example_reviews[1]
    st.rerun()

if col3.button("Example 3"):
    st.session_state.review_text = example_reviews[2]
    st.rerun()
