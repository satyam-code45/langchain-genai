from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 =  ChatOpenAI()

model2 =  ChatOpenAI()

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short questions quiz along with from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2  | parser
})

merger_chain = prompt3 | model1 | parser

chain = parallel_chain | merger_chain

text = '''
Embeddings are numerical representations of real-world objects that machine learning (ML) and artificial intelligence (AI) systems use to understand complex knowledge domains like humans do. As an example, computing algorithms understand that the difference between 2 and 3 is 1, indicating a close relationship between 2 and 3 as compared to 2 and 100. However, real-world data includes more complex relationships. For example, a bird-nest and a lion-den are analogous pairs, while day-night are opposite terms. Embeddings convert real-world objects into complex mathematical representations that capture inherent properties and relationships between real-world data. The entire process is automated, with AI systems self-creating embeddings during training and using them as needed to complete new tasks.

Embeddings enable deep-learning models to understand real-world data domains more effectively. They simplify how real-world data is represented while retaining the semantic and syntactic relationships. This allows machine learning algorithms to extract and process complex data types and enable innovative AI applications. The following sections describe some important factors. 

Reduce data dimensionality
Data scientists use embeddings to represent high-dimensional data in a low-dimensional space. In data science, the term dimension typically refers to a feature or attribute of the data. Higher-dimensional data in AI refers to datasets with many features or attributes that define each data point. This can mean tens, hundreds, or even thousands of dimensions. For example, an image can be considered high-dimensional data because each pixel color value is a separate dimension.

When presented with high-dimensional data, deep-learning models require more computational power and time to learn, analyze, and infer accurately. Embeddings reduce the number of dimensions by identifying commonalities and patterns between various features. This consequently reduces the computing resources and time required to process raw data.

Train large language models
Embeddings improve data quality when training large language models (LLMs). For example, data scientists use embeddings to clean the training data from irregularities affecting model learning. ML engineers can also repurpose pre-trained models by adding new embeddings for transfer learning, which requires refining the foundational model with new datasets. With embeddings, engineers can fine-tune a model for custom datasets from the real world.

Build innovative applications
Embeddings enable new deep learning and generative artificial intelligence (generative AI) applications. Different embedding techniques applied in neural network architecture allow accurate AI models to be developed, trained, and deployed in various fields and applications. For example:

With image embeddings, engineers can build high-precision computer vision applications for object detection, image recognition, and other visual-related tasks. 
With word embeddings, natural language processing software can more accurately understand the context and relationships of words.
Graph embeddings extract and categorize related information from interconnected nodes to support network analysis.
Computer vision models, AI chatbots, and AI recommender systems all use embeddings to complete complex tasks that mimic human intelligence
'''

result = chain.invoke({'text' : text})

print(result)

chain.get_graph().print_ascii()