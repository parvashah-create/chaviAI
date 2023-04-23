import spacy
import re
import emoji

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')



def preprocess_tweet(tweet):
    """
    Preprocesses a tweet for sentiment analysis by performing the following steps:
    1. Removing URLs and mentions
    2. Converting emojis to their descriptions
    3. Removing punctuation and converting to lowercase
    4. Tokenizing the tweet into words
    5. Removing stop words
    6. Lemmatizing words
    
    Args:
    tweet (str): The tweet to preprocess
    
    Returns:
    preprocessed_tweet (str): The preprocessed tweet
    """
    
    # Remove URLs and mentions
    tweet = re.sub(r"http\S+|www\S+|https\S+|@\S+", "", tweet)
    
    # Convert emojis to their descriptions
    tweet = emoji.demojize(tweet)
    tweet = re.sub(r":\S+:", lambda m: " ".join(m.group(0).replace(":", "").replace("_", " ").split()), tweet)
    
    # Remove punctuation and convert to lowercase
    tweet = re.sub(r"[^\w\s]", "", tweet)
    tweet = tweet.lower()
    
    # Tokenize the tweet into words
    doc = nlp(tweet)
    words = [token.text for token in doc]
    
    # Remove stop words
    words = [word for word in words if not nlp.vocab[word].is_stop]
    
    # Lemmatize words
    words = [token.lemma_ for token in nlp(" ".join(words))]
    
    # Join the words back into a string
    preprocessed_tweet = " ".join(words)
    
    return preprocessed_tweet

# print(preprocess_tweet("I need @SHEIN_Official to take me to Coachella next year I’m always wearing shein to festivals 😏"))
