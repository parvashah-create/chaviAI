import time
import pinecone
import openai 
from decouple import config
from vector_search_engine.pinecone_utils import PineconeUtils


pinecone_utils = PineconeUtils(config("PINECONE_API_KEY"),config("PINECONE_ENV"))


# print(pinecone_utils.initialize_index("s-ai",512))
pinecone.init(api_key=config("PINECONE_API_KEY"), environment=config("PINECONE_ENV"))
# print(pinecone.list_indexes())

# print(pinecone_utils.get_index_list())
# # print(pinecone.delete_index("chhavi-ai"))
# print(pinecone_utils.initialize_index("chhavi-ai",768))
# print(pinecone_utils.get_index_list())
index_description = pinecone.describe_index("chhavi-ai")
print(index_description)
# index = pinecone.Index("chhavi-ai") 


