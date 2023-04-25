import streamlit as st
import openai
from database_utils.db_utils import DbUtils
from prompt.prompt_eng import create_prompt, generate_response
from decouple import config



def create_prompt(text):

    context = """
    \n The above is a list of some recent positive and negative tweets regarding the company shein,
    analyze the tweets and generate a Brand Image Management report which states a brand image score out of 100 the things customers like,
    major problems faced by customers and also suggest remedies for the same in markdown format
    
    """
    prompt = str(text) + context

    return prompt
    

def generate_response(prompt):
    openai.api_key = config("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response = completion.choices[0].message
    return response["content"]

db_utils = DbUtils("tweet.db")


# st.title("ChhaviAI")
# tweets  = db_utils.get_recent_sentiments("shein_tweets")
# prompt  = create_prompt(tweets)
# response  = generate_response(prompt)
# st.write(response)
