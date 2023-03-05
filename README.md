# CustomerVoice: Sentiment Analysis for Actionable Customer Feedback

CustomerVoice is a sentiment analysis project that helps companies analyze customer feedback and gain valuable insights into their products and services. With CustomerVoice, you can collect customer feedback from various sources such as social media, surveys, online reviews, and customer support tickets, and analyze the sentiment to identify areas for improvement.


## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#Installation)
- [Usage](#usage)
- [License](#license)

## Getting Started
To get started with CustomerVoice, you will need to clone the repository and install the necessary dependencies.

```
# Clone the repository
git clone https://github.com/AnthonyByansi/CustomerVoice.git

# Install the dependencies
pip install -r requirements.txt
```

## Prerequisites
CustomerVoice requires the following dependencies:

* Python 3.x
* pandas
*  numpy
* nltk
* scikit-learn
* matplotlib
* seaborn

## Installation
To install CustomerVoice, you can use pip: `pip install customervoice`

Alternatively, you can clone the repository and install it manually: 
```
git clone https://github.com/AnthonyByansi/CustomerVoice.git
cd CustomerVoice
python setup.py install
```
## Usage

To use **CustomerVoice** , you will need to collect customer feedback data and `preprocess` it to remove any irrelevant information such as URLs, hashtags, and mentions. You can use the preprocess module to clean and normalize the data.

```
from customervoice.preprocess import clean_text

# Clean and normalize the text
text = "This product is amazing! I love it so much! #bestproductever"
clean_text(text)
# Output: "product amazing love much"
```

Next, you can use the `sentiment` module to perform sentiment analysis on the customer feedback. CustomerVoice supports both rule-based and machine learning methods for sentiment analysis
