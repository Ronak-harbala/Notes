from langchain_community.document_loaders import WebBaseLoader

url = "https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03"

data = WebBaseLoader(url)
data = data.load()
print(len(data))