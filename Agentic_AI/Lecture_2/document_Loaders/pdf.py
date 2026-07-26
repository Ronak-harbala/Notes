from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document_Loaders/lorem_001.pdf")
data = data.load()

print(len(data))