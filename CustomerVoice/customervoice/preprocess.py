import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def clean_text(text):
    # remove punctuation and convert to lowercase
    cleaned_text = ''.join([c.lower() for c in text if c.isalpha() or c.isspace()])
    return cleaned_text

def tokenize_text(text):
    # tokenize text into words
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    # remove stopwords from tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

def stem_words(tokens):
    # stem words using Porter stemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def preprocess_feedback(df):
    # preprocess customer feedback DataFrame
    df['cleaned_text'] = df['text'].apply(lambda x: clean_text(x))
    df['tokenized_text'] = df['cleaned_text'].apply(lambda x: tokenize_text(x))
    df['filtered_text'] = df['tokenized_text'].apply(lambda x: remove_stopwords(x))
    df['stemmed_text'] = df['filtered_text'].apply(lambda x: stem_words(x))
    return df
