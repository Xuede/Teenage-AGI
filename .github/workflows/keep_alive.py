import os
import pinecone

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
index_name = 'my-agent'

try:
    client = pinecone.Client(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

    # Fetch some info to keep the index alive
    info = pinecone.info(index_name)
    print(f"Index info: {info}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    pinecone.deinit()
