import streamlit as st
import requests
import time

fastapi_url = "http://127.0.0.1:8000"
# fastapi_url = "http://54.86.128.1:9000"


# Set page title and favicon
st.set_page_config(page_title="ChhaviAI", page_icon=":robot_face:")

# Set page header
st.title(":robot_face: ChhaviAI")

# Brand Image Report Section
st.header("Brand Image Report")

# User input for Twitter username
username = st.text_input("Enter Twitter username:")

# Generate report button
if st.button("Generate Report") and username != "":
    with st.spinner("Generating report..."):
        response = requests.get(f"{fastapi_url}/brand-image-report/{username}")
        st.write(response.json()["response"])


# Product Evaluation Section
st.header("Product Evaluation")

# User input for product query
query = st.text_input("Enter a product query:")

# Ask button
if st.button("Ask") and query != "":
    with st.spinner("Fetching product evaluation..."):
        json={"query": f"{query}"}
        response = requests.post(f"{fastapi_url}/vector-search/",json=json)
        st.write(response.json()["response"])
