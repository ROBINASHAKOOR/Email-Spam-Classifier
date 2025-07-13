import nltk
import re
import string
import joblib
import joblib
import streamlit as st     
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# download once
nltk.download('stopward')
nltk.download('wordnet')

# Load model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
 
# Preprocessing function
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Streamlit UI
st.title(" Email Spam Classifier")
st.write("Enter a message below to check if it's Spam or Not.")

message = st.text_area("Enter your email or SMS message here:")

if st.button("Classify"):
    if message.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        clean_msg = preprocess(message)
        message_vec = vectorizer.transform([clean_msg])
        prediction = model.predict(message_vec)[0]
        if prediction == 1:
            st.error(" This is a SPAM message!")
        else:
            st.success(" This is a legitimate message (HAM).")
