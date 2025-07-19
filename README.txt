#  Email Spam Classifier using Machine Learning

This project classifies email or SMS messages as **Spam** or **Not Spam (Ham)** using machine learning models.

---

##  Features
- Preprocessing: lowercasing, punctuation removal, stopword removal, lemmatization
- Models used:
  - Logistic Regression (Best performance)
  - Multinomial Naive Bayes
  - Random Forest
- TF-IDF vectorization for feature extraction
- Streamlit app for live testing

---
For security reasons, the `.env` file is **NOT included** in this repository.

Before running the project, create a `.env` file in the root directory with the following variables:


##  Files Included
- `spam_classifier.ipynb` – Jupyter Notebook for training and evaluation
- `app.py` – Streamlit app for real-time message classification
- `spam_model.pkl` – Saved trained model
- `tfidf_vectorizer.pkl` – Saved vectorizer
- `spam.csv` – SMS Spam Collection dataset (Kaggle source)
- `README.md` – Project overview

---

## How to Run
streamlit run spam.py
