from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following questions - \n {ques} from the following text - \n {text}',
    input_variables=['ques','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m4-16-gb-512-gb-ssd-macos-sequoia-mw133hn-a/p/itma6c9abac7d313?pid=COMH9ZWQWFCGN73J&lid=LSTCOMH9ZWQWFCGN73J8CEOQ6&marketplace=FLIPKART&q=macbook%20air%20m4&sattr[]=color&sattr[]=system_memory&sattr[]=ssd_capacity&sattr[]=screen_size&st=system_memory'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    'ques': 'Tell me the features, advantages, disadvantages of Mackbook air M4 in 3 points each?',
    'text': docs[0].page_content
})

print(result)