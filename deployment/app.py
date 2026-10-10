import os
import re
import string
import unicodedata

import joblib
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download the NLTK resources the cleaner needs (quietly)
for pkgName in ["stopwords", "wordnet", "omw-1.4"]:
    nltk.download(pkgName, quiet=True)

stopWords = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# Same cleaning function used when the model was trained (Question 1.1)
def cleanText(text):
    # Normalise unicode and drop leftover non-ASCII symbols
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode()
    # Fix section headers glued to the text, e.g. "BackgroundGame"
    text = re.sub(r"\b(Background|Objectives?|Methods?|Results|Conclusions?|Purpose)(?=[A-Z])", r"\1 ", text)
    # Remove boilerplate, URLs, citation markers and copyright lines
    text = re.sub(r"[^.]*(download this paper|www\.nber\.org)[^.]*\.", " ", text, flags=re.I)
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\[\d+(?:[,\-]\s*\d+)*\]", " ", text)
    text = re.sub(r"copyright\s*\d{4}[^.]*\.", " ", text, flags=re.I)
    # Lowercase, remove numbers and punctuation
    text = text.lower()
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
    # Remove stopwords and short tokens, then lemmatize
    return " ".join(lemmatizer.lemmatize(word) for word in text.split()
                    if word not in stopWords and len(word) > 2)


# Load the saved model once and reuse it between clicks
@st.cache_resource
def loadModel():
    return joblib.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "researchlyModel.pkl"))


model = loadModel()

# Page layout
st.title("Researchly Research Abstract Classifier")
st.write("This app classifies research abstracts as either AI-related or classical research.")

abstractInput = st.text_area("Enter research abstract:", height=250)

if st.button("Classify Abstract"):
    if abstractInput.strip() == "":
        st.warning("Please enter an abstract first.")
    else:
        # Clean the text, then predict (1 = ai, 0 = classical)
        cleanedAbstract = cleanText(abstractInput)
        prediction = model.predict([cleanedAbstract])[0]
        labelName = "artificial intelligence" if prediction == 1 else "classical research"

        st.subheader("Prediction")
        st.success(f"The abstract is classified as: {labelName}")
