from typing import Union
from fastapi_utils.tasks import repeat_every
from fastapi import FastAPI
from pydantic import BaseModel
from data_pipeline import pipeline
from database_utils.db_utils import DbUtils
from prompt.openai_utils import create_prompt, generate_response, generative_search

db_utils = DbUtils("tweet.db")

app = FastAPI()

class StringInput(BaseModel):
    query: str


# @app.on_event("startup")
# @repeat_every(seconds=300)  # 1 hour
# def run_pipline() -> None:
#     pipeline()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/brand-image-report/{username}")
def brand_image_report(username):
    new_tweets = pipeline(username)
    if new_tweets:
        tweets  = db_utils.get_recent_sentiments("tweets",username)
        prompt  = create_prompt(tweets)
        response  = generate_response(prompt)
    else:
        response = "Pipeline error!"    
    return {"response":response}

@app.post("/vector-search/")
def vector_search(string_input: StringInput):
    response = generative_search(string_input.query)
    return {"response":response}
