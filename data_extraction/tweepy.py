import requests
import os
import json
import pandas as pd

class TwitterUtils:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
        self.tweet_search_url = "https://api.twitter.com/2/tweets/search/recent"
        self.user_search_url = "https://api.twitter.com/2/users"

    def bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """
        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r

    def connect_to_endpoint(self, url, params):
        response = requests.get(url, auth=self.bearer_oauth, params=params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def search_tweets(self, query, max_tweets, tweet_fields):
        query_params = {'query': query,'max_results': max_tweets, 'tweet.fields': tweet_fields}
        json_response = self.connect_to_endpoint(self.tweet_search_url, query_params)
        return json_response
    
    def search_users(self, ids, user_fields):
        query_params = {'ids': ids,'user.fields': user_fields}
        json_response = self.connect_to_endpoint(self.user_search_url, query_params)
        return json_response


# twitter_scrapper = TwitterUtils("AAAAAAAAAAAAAAAAAAAAAAJCmwEAAAAAC0asMgYmegba5FonDLKr%2BcwF4Lc%3DEtuiAKzEKiZlTNHeE2CJwnukAMBWeaJHeyWtuLVoA01uEKC9P1")

# # res_json = twitter_scrapper.search_tweets('@Apple lang:en',10,'author_id,created_at,lang,public_metrics,entities')

# res_json = twitter_scrapper.search_users('879412528358490113,1088492715145195520','id,location,username,name,created_at')

# # latest_tweets=[]
# # for i in res_json["data"]:
# #     print(i["text"])
# #     latest_tweets.append((i["id"],i["author_id"], i["created_at"],i["text"], i["public_metrics"]["impression_count"],i["public_metrics"]["like_count"]))

# # latest_tweets_db = pd.DataFrame(latest_tweets,columns=["id","author_id","created_at","text","impression_count","like_count"])
# # print(latest_tweets_db)
# print(json.dumps(res_json, indent=4, sort_keys=True))