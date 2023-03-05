import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def train_sentiment_model(df):
    # train sentiment analysis model using Naive Bayes
    cv = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
    X = cv.fit_transform(df['stemmed_text'].apply(lambda x: ' '.join(x)))
    y = df['sentiment']
    model = MultinomialNB()
    model.fit(X, y)
    return cv, model

def predict_sentiment(cv, model, text):
    # predict sentiment of text using pre-trained model
    X = cv.transform([text])
    sentiment = model.predict(X)[0]
    return sentiment
