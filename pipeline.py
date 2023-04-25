from data_extraction.tweepy import TwitterUtils
from database_utils.db_utils import DbUtils
from data_extraction.preprocessor import preprocess_tweet
from sentimental_analysis.model_utils import SentimentAnalyzer
from vector_search_engine.embeddings_utils import EmbeddingsUtil
from vector_search_engine.pinecone_utils import PineconeUtils
from decouple import config
import pandas as pd
import sqlite3

twitter_scrapper = TwitterUtils("AAAAAAAAAAAAAAAAAAAAAAJCmwEAAAAAC0asMgYmegba5FonDLKr%2BcwF4Lc%3DEtuiAKzEKiZlTNHeE2CJwnukAMBWeaJHeyWtuLVoA01uEKC9P1")
db_utils = DbUtils("tweet.db")
senti_model = SentimentAnalyzer()
embeds = EmbeddingsUtil()
pinecone_utils = PineconeUtils(config("PINECONE_API_KEY"),config("PINECONE_ENV"))


# vectors=[
#         {
#         'id':'vec1', 
#         'values':[0.1, 0.2, 0.3, 0.4], 
#         'metadata':{'genre': 'drama'},
#            'sparse_values':
#            {'indices': [10, 45, 16],
#            'values':  [0.5, 0.5, 0.2]}},
#         {'id':'vec2', 
#         'values':[0.2, 0.3, 0.4, 0.5], 
#         'metadata':{'genre': 'action'},
#            'sparse_values':
#            {'indices': [15, 40, 11],
#            'values':  [0.4, 0.5, 0.2]}}
#     ]

def pipeline():

    res_json = twitter_scrapper.search_tweets('@SHEIN_Official lang:en -is:retweet -is:reply -has:links ',100,'author_id,created_at,lang,public_metrics,entities')
    latest_tweets=[]
    vectors = []
    db_id_list = db_utils.get_id_list("shein_tweets")
    for i in res_json["data"]:
        if i["id"] not in db_id_list:
            text = preprocess_tweet(i["text"])
            sentiment_label = senti_model.analyze_sentiment(text)
            embed = embeds.mpnet_embeddings(text)
            vectors.append({'id':i["id"], 'values':embed, 'metadata':{'created_at': i["created_at"],'impression_count':i["public_metrics"]["impression_count"],'like_count':i["public_metrics"]["like_count"],'sentiment_label':sentiment_label}})
            latest_tweets.append((i["id"],i["author_id"], i["created_at"],text, i["public_metrics"]["impression_count"],i["public_metrics"]["like_count"],sentiment_label))
    print(latest_tweets)
    if latest_tweets and vectors:
        pinecone_utils.upsert_vectors(vectors,"chhavi-ai")
        latest_tweets_df = pd.DataFrame(latest_tweets,columns=["id","author_id","created_at","text","impression_count","like_count","sentiment_label"])
        db_utils.append_sqlite_table(latest_tweets_df,"shein_tweets")

    return True


print(pipeline())