import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")


def text_analysis(data):
    stop_words = set(stopwords.words("english"))
    ps = PorterStemmer()

    def preprocess_text(text):
        if isinstance(text, str) and text.strip():
            tokens = word_tokenize(text.lower())
            tokens = [
                word
                for word in tokens
                if word not in stop_words and word not in string.punctuation
            ]
            tokens = [ps.stem(word) for word in tokens]
            return " ".join(tokens)
        else:
            return ""

    data["Preprocessed Text"] = data["Review Text"].apply(preprocess_text)

    def text_similarity(text1, text2):
        if text1 and text2:
            vectorizer = CountVectorizer().fit_transform([text1, text2])
            vectors = vectorizer.toarray()
            return cosine_similarity(vectors)[0, 1]
        else:
            return 0.0

    similar_reviews = {}

    for division in data["Division Name"].unique():
        division_reviews = data[data["Division Name"] == division]["Preprocessed Text"]
        for idx, review1 in enumerate(division_reviews):
            similar_reviews[idx] = []
            for jdx, review2 in enumerate(division_reviews):
                if idx != jdx:
                    similarity_score = text_similarity(review1, review2)
                    if similarity_score > 0.7:
                        similar_reviews[idx].append(jdx)

    similar_reviews_output = {}
    for idx, similar_idxs in similar_reviews.items():
        if similar_idxs:
            similar_reviews_output[idx] = similar_idxs

    return similar_reviews_output
