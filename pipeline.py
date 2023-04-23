from data_extraction.tweepy import TwitterUtils
from database_utils.db_utils import DbUtils
from data_extraction.preprocessor import preprocess_tweet
import 
import pandas as pd
import sqlite3

twitter_scrapper = TwitterUtils("AAAAAAAAAAAAAAAAAAAAAAJCmwEAAAAAC0asMgYmegba5FonDLKr%2BcwF4Lc%3DEtuiAKzEKiZlTNHeE2CJwnukAMBWeaJHeyWtuLVoA01uEKC9P1")
db_utils = DbUtils("tweet.db")

def create_tweepy_df():

    res_json = twitter_scrapper.search_tweets('@SHEIN_Official lang:en -is:retweet -is:reply -has:links ',10,'author_id,created_at,lang,public_metrics,entities')

    latest_tweets=[]
    for i in res_json["data"]:
        text = preprocess_tweet(i["text"])

        latest_tweets.append((i["id"],i["author_id"], i["created_at"],text, i["public_metrics"]["impression_count"],i["public_metrics"]["like_count"]))

    latest_tweets_df = pd.DataFrame(latest_tweets,columns=["id","author_id","created_at","text","impression_count","like_count"])
    return latest_tweets_df



tweet_df = create_tweepy_df()
text_list = tweet_df["text"].to_list()
print(text_list)
db_utils.append_sqlite_table(tweet_df,"shein_tweets")
