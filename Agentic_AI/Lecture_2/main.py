from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()

data = PyPDFLoader("document_Loaders/lorem_001.pdf")
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [("system", "You are a AI who summarize text."),
      ("human", "{data}")]
)

prompt = template.format_messages(data = docs[0].page_content)

model = ChatMistralAI(model="mistral-small-2603")
result = model.invoke(prompt)
print(result.content)

