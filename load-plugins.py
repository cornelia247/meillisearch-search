import meilisearch
import json

client = meilisearch.Client('http://localhost:7700', 'masterKey')

# An index is where the documents are stored.
index = client.index('plugins')

# Load documents from a file
with open('plugins.json', 'r') as f:
    documents = json.load(f)

# If the index 'movies' does not exist, Meilisearch creates it when you first add the documents.
index.add_documents(documents)
