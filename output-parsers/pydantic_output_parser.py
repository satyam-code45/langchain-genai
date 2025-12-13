from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):

    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the Person", gt=18)
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate  the name, age and city of a ficitonal person from country {country} \n {format_instruction}',
    input_variables=['country'],
    partial_variables={'format_instruction': parser.get_format_instructions}
)

# prompt = template.invoke({'country': 'India'})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

# using chains

chain = template | model | parser

final_result = chain.invoke({'country': 'America'})

print(final_result)