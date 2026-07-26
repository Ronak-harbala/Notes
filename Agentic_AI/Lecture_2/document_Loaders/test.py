from langchain_community.document_loaders import TextLoader

data = TextLoader("document_Loaders/notes.txt")
data = data.load()
print(data[0].page_content)