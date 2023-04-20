import torch
from transformers import BertTokenizer, BertModel, RobertaTokenizer, RobertaModel, XLNetTokenizer, XLNetModel
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
class SentimentAnalyzer:
    
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.bert_model = BertModel.from_pretrained('bert-base-uncased').to(self.device)
        self.bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.roberta_model = RobertaModel.from_pretrained('roberta-base').to(self.device)
        self.roberta_tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
        self.vader_model = SentimentIntensityAnalyzer()

    def bert_sentiment(self, text):
        inputs = self.bert_tokenizer(text, return_tensors='pt').to(self.device)
        outputs = self.bert_model(**inputs)
        pooled_output = outputs.pooler_output
        pooled_output = pooled_output.mean(dim=1)  # take the mean along the second dimension
        sentiment = torch.tanh(pooled_output)
        return sentiment[0].item()  # extract the first element, which is a scalar


    def roberta_sentiment(self, text):
        inputs = self.roberta_tokenizer(text, return_tensors='pt').to(self.device)
        outputs = self.roberta_model(**inputs)
        pooled_output = outputs.pooler_output
        pooled_output = pooled_output.mean(dim=1)  # take the mean along the second dimension
        sentiment = torch.tanh(pooled_output)
        return sentiment[0].item()  # extract the first element, which is a scalar


    def textblob_sentiment(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        return (sentiment + 1) / 2  # scale to [0, 1]
    
    def vader_sentiment(self, text):
        sentiment = self.vader_model.polarity_scores(text)
        return sentiment
    
    def analyze_sentiment(self, text):
        bert_sentiment = self.bert_sentiment(text)
        roberta_sentiment = self.roberta_sentiment(text)
        textblob_sentiment = self.textblob_sentiment(text)
        vader_sentiment = self.vader_sentiment(text)

        return {'bert_sentiment': bert_sentiment,
                'roberta_sentiment': roberta_sentiment,
                'textblob_sentiment': textblob_sentiment,
                'vader_sentiment': vader_sentiment}
    


senti_model = SentimentAnalyzer()
print(senti_model.analyze_sentiment("The Iphone 13 is bad"))