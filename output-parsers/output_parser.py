from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

#1st Prompt
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


#2nd Prompt
template2 = PromptTemplate(
    template='Write a five line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'balck hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result2 = model.invoke(prompt2)

print(result2.content)