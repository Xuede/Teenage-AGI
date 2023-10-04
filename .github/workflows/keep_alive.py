import os
import pinecone

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
index_name = 'my-agent'

# Fetch some info to keep the index alive
info = pinecone.info(index_name)
print(f"Index info: {info}")

pinecone.deinit()
