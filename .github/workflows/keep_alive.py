import os
from pinecone import Client

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
index_name = 'my-agent'

try:
    client = Client(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

    # Fetch some info to keep the index alive
    info = client.info(index_name)
    print(f"Index info: {info}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
