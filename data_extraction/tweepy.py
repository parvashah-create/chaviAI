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

