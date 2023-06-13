# ChhaviAI  
Brand Image Management Solution: [Demo](https://parvashah-create-chhavi-streamlit-app-7izrgq.streamlit.app/)

## Description
This project is designed to extract recent tweets, preprocess them, pass them through a sentimental analysis model to extract sentiment, and store the results in a SQLite database. It simultaneously generates embeddings to store in Pinecone vector database. The project extracts the most recent positive and negative tweets from the SQLite database, passes them as context to ChatGPT, and produces a brand image report.

Users can also query specific products by generating embeddings of the query and performing cosine similarity searches. The project retrieves relevant tweet IDs from Pinecone and gets relevant tweets from the SQLite database. It then passes the tweets as context to ChatGPT, which produces an image evaluation for that product.

## Installation
1. Clone the repository
```bash
git clone https://github.com/parvashah-create/chaviAI.git
```
2. Create a virtual environment and activate it
``` bash
python3 -m venv env
source env/bin/activate
```

3. Install the required packages
``` bash
pip install -r requirements.txt
```
4. Create a file named .env and add the following environment variables
``` makefile
TWITTER_API_KEY=<your_twitter_api_key>
TWITTER_API_SECRET=<your_twitter_api_secret>
TWITTER_ACCESS_TOKEN=<your_twitter_access_token>
TWITTER_ACCESS_SECRET=<your_twitter_access_secret>
PINECONE_API_KEY=<your_pinecone_api_key>
```
## Usage
1. Run main.py to extract recent tweets, preprocess them, pass them through a sentimental analysis model, and store the results in a SQLite database. It will simultaneously generate embeddings to store in Pinecone vector database.

2. To produce a brand image report, run brand_image_report.py.

3. To perform a cosine similarity search and retrieve relevant tweets for a specific product, run product_evaluation.py.

## Resources

- Documentation - [Sentimental-Analysis-Brand-Image-Management - Report](https://codelabs-preview.appspot.com/?file_id=https://docs.google.com/document/d/1gUDWp26tWl7Pfkdf3xpmKN5onOkNFOuHQw6HxB__7ag/edit?usp=sharing#0)
- Streamlit Application - [Sentimental-Analysis-Brand-Image-Management - Application](https://parvashah-create-chhavi-streamlit-app-7izrgq.streamlit.app/)
- Video Demonstration - [Sentimental-Analysis-Brand-Image-Management - Video](https://www.loom.com/share/51edb70b26f64e239bb97a74352b026d)

## Credits
This project was created by [Utkarsh Dhande](https://github.com/utkarshdhande) and [Parva Shah](https://github.com/parvashah-create). It was made possible thanks to the following libraries and APIs:

- Tweepy
- TextBlob
- Pandas
- Scikit-learn
- Pinecone
- OpenAI GPT-3.5
