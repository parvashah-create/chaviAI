import torch
from transformers import BertTokenizer, BertModel, RobertaTokenizer, RobertaModel, AutoModelForSequenceClassification, AutoTokenizer
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import numpy as np
from scipy.special import softmax


class SentimentAnalyzer:
    
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.roberta_tweet_model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.roberta_tweet_tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.vader_model = SentimentIntensityAnalyzer()


    def roberta_tweet_sentiment(self,text):
        encoded_input = self.roberta_tweet_tokenizer(text, return_tensors='pt').to(self.device)
         # Make prediction and get scores
        output = self.roberta_tweet_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        if ranking[0] == 0:
            label = 'neg'
        elif ranking[0] == 1:
            label = 'neu'
        elif ranking[0] == 2:
            label = 'pos'
        return label

    
    def textblob_sentiment(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment < 0:
            label = 'neg'
        elif sentiment == 0:
            label = 'neu'
        elif sentiment > 0:
            label = 'pos'
        return label 
       
    def naive_bayes_sentiment(self, text):
        blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
        sentiment = blob.sentiment.classification
        return sentiment  
    
    def vader_sentiment(self, text):
        sentiment = self.vader_model.polarity_scores(text)
        # Remove the 'compound' key from the dictionary
        del sentiment['compound']
        # Get the key with the maximum value
        label = max(sentiment, key=sentiment.get)
        return label
    
    def analyze_sentiment(self, text):
        roberta_tweet_sentiment = self.roberta_tweet_sentiment(text)
        textblob_sentiment = self.textblob_sentiment(text)
        naive_bayes_sentiment = self.naive_bayes_sentiment(text)
        vader_sentiment = self.vader_sentiment(text)

        model_sentiments =  {
                'roberta_tweet_sentiment': roberta_tweet_sentiment,
                'textblob_sentiment': textblob_sentiment,
                'naive_bayes_sentiment': naive_bayes_sentiment,
                'vader_sentiment': vader_sentiment
                }
        sentiment_counts = Counter(model_sentiments.values())
        most_common_sentiment = sentiment_counts.most_common(1)[0][0]
        return most_common_sentiment


# senti_model = SentimentAnalyzer()
# text = "['new iphone suck hate', 'sucks', 'hate']"
# text = "@meta super frustrated access husband account take solution help contact form work nightmare"
# text = "@meta is awesome and I love using it."
# text = "sun sets in the west"
# text = "['frustrate', 'access', 'husband', 'account', 'take', 'solution', 'help', 'contact', 'form', 'work', 'nightmare']"
# text = """this is honestly 🔥🔥🔥"""
# print(text)
# print(senti_model.analyze_sentiment(text))


# {'bert_sentiment': 0.0011509765172377229, 'roberta_sentiment': 0.005614308640360832, 'roberta_tweet_sentiment': 'neg', 'textblob_sentiment': -0.18333333333333332, 'naive_bayes_sentiment': 'pos', 'vader_sentiment': 'neu'}