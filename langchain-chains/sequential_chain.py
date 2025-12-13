from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Give me in deatil description about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Based on this \n {description}  \n Generate a five most important pointer '
)

chain = prompt1 | model | parser | prompt2 | model | parser

result =  chain.invoke({'topic': 'Unemployment in India'})

print(result)

chain.get_graph().print_ascii()