import streamlit as st
import requests



fastapi_url = "http://127.0.0.1:8000"

st.title("ChhaviAI")

username = st.text_input("Enter twitter username")
if st.button("Generate Report"):
    response = requests.get(f"{fastapi_url}/brand-image-report/{username}")
    st.write(response.json()["response"])



query = st.text_input('Ask question about a specific product')

if st.button("Ask"):
    json={"query": f"{query}"}
    response = requests.post(f"{fastapi_url}/vector-search/",json=json)
    st.write(response.json()["response"])
