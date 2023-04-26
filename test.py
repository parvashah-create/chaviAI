import time
import pinecone
import openai 
from decouple import config
import io
from vector_search_engine.pinecone_utils import PineconeUtils

# def transcribe_audio(file_path: str, model: str) -> str:
#     """
#     Transcribes an audio file using the OpenAI API.

#     Args:
#         api_key (str): The OpenAI API key.
#         file_path (str): The path to the audio file.
#         model (str): The name of the OpenAI model to use for transcription.

#     Returns:
#         str: The transcription of the audio file.

#     Example:
#         api_key = os.getenv("OPENAI_API_KEY")
#         file_path = "Apple Think Different - Steve Jobs Narrated Version.mp3"
#         model = "whisper-1"

#     """
#     openai.api_key = config("OPENAI_API_KEY")
#     audio_file = open(file_path, "rb")
#     transcript = openai.Audio.transcribe(model, audio_file)
#     return transcript["text"]

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# openai.api_key = config("OPENAI_API_KEY")
# audio_file= open("/Users/parvashah/Downloads/WhatsApp Audio 2023-04-23 at 11.55.38 AM.m4a", "rb")

# transcript = openai.Audio.transcribe("whisper-1", audio_file)
# print(transcript["text"])
# pinecone_utils = PineconeUtils(config("PINECONE_API_KEY"),config("PINECONE_ENV"))


# # print(pinecone_utils.initialize_index("s-ai",512))
# pinecone.init(api_key=config("PINECONE_API_KEY"), environment=config("PINECONE_ENV"))
# # print(pinecone.list_indexes())

# # print(pinecone_utils.get_index_list())
# # # print(pinecone.delete_index("chhavi-ai"))
# # print(pinecone_utils.initialize_index("chhavi-ai",768))
# # print(pinecone_utils.get_index_list())
# index_description = pinecone.describe_index("chhavi-ai")
# print(index_description)
# # index = pinecone.Index("chhavi-ai") 


