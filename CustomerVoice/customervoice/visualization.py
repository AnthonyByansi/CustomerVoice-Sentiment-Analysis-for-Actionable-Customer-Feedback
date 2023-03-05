import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def plot_sentiment_distribution(df):
    # create bar chart of sentiment distribution
    sentiment_counts = df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def generate_word_cloud(df):
    # generate word cloud from customer feedback
    feedback_text = ' '.join(df['cleaned_text'].tolist())
    wordcloud = WordCloud(background_color='white').generate(feedback_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
