import openai 
from decouple import config
import time
from sentence_transformers import SentenceTransformer



class EmbeddingsUtil:
    def __init__(self):
        pass

    def openai_embeddings(self, texts, embed_model):
        """
        Create embeddings for given texts using OpenAI's GPT-3 model.

        Args:
            texts (list): List of texts for which embeddings need to be created.
            embed_model (str): Engine name for embedding model, e.g. "text-davinci-002".

        Returns:
            list: List of embeddings for the given texts.
        """
        openai.api_key =config("OPENAI_API_KEY")
        try:
            res = openai.Embedding.create(input=texts, engine=embed_model)
        except openai.error.RateLimitError:
            done = False
            while not done:
                time.sleep(5)
                try:
                    res = openai.Embedding.create(input=texts, engine=embed_model)
                    done = True
                except openai.error.RateLimitError:
                    pass
        embeds = [record['embedding'] for record in res['data']]
        return embeds
    
    def mpnet_embeddings(self, text):
        model = SentenceTransformer('all-mpnet-base-v2')

        embedding = model.encode(text,show_progress_bar=True)

        return embedding
    


# embeds = EmbeddingsUtil()
# print(embeds.mpnet_embeddings("This is a good day"))