import streamlit as st
import openai
from database_utils.db_utils import DbUtils
from vector_search_engine.pinecone_utils import PineconeUtils
from vector_search_engine.embeddings_utils import EmbeddingsUtil
from decouple import config




pinecone_utils = PineconeUtils(config("PINECONE_API_KEY"),config("PINECONE_ENV"))
embeds_utils = EmbeddingsUtil()

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

def generative_search(query):
    query_embeds = embeds_utils.mpnet_embeddings(query)
    vec_search = pinecone_utils.search_index("chhavi-ai",10,query_embeds.tolist())
    search_ids = [x['id'] for x in vec_search['matches']]
    print(search_ids)
    context = db_utils.get_id_text("shein_tweets",tuple(search_ids))
    prompt = f"{context}" + f"\n Analyze the tweets and their sentiments above and give a report on how customers are recieving the product {query}"
    response = generate_response(prompt)
    return response

db_utils = DbUtils("tweet.db")


st.title("ChhaviAI")

if st.button("Generate Report"):
    tweets  = db_utils.get_recent_sentiments("shein_tweets")
    prompt  = create_prompt(tweets)
    response  = generate_response(prompt)
    st.write(response)

query = st.text_input('Ask question about a specific product')

if st.button("Ask"):
    response = generative_search(query)
    st.write(response)
