from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

cricketers_docs = [
    {
        "id": "rohit_sharma",
        "text": """Rohit Sharma is a right-handed opening batsman known for his elegant stroke play 
and ability to score big hundreds in limited overs cricket. He has captained India and Mumbai Indians, 
and is admired for his calm leadership and explosive batting.""",
    },
    {
        "id": "virat_kohli",
        "text": """Virat Kohli is one of the most consistent and aggressive top-order batsmen in modern cricket. 
Known for his fitness, chase mastery, and strong technique, he has been a former captain of India 
and plays for Royal Challengers Bangalore.""",
    },
    {
        "id": "ms_dhoni",
        "text": """MS Dhoni, a legendary wicketkeeper-batsman and captain, is famous for his calm mindset, 
tactical intelligence, and exceptional finishing ability in limited overs cricket. He led India to multiple ICC trophies 
and captains Chennai Super Kings in the IPL.""",
    },
    {
        "id": "sachin_tendulkar",
        "text": """Sachin Tendulkar is considered one of the greatest batters in cricket history. 
Known for his classical technique, longevity, and unmatched influence on the game, he inspired generations 
of cricketers with his excellence across formats.""",
    },
    {
        "id": "jasprit_bumrah",
        "text": """Jasprit Bumrah is a world-class fast bowler known for his unique action, sharp yorkers, 
and ability to perform under pressure. He is one of India's most reliable bowlers in death overs 
and a consistent wicket-taker across formats.""",
    },
]

query = "tell me about virat kohli"

# FIX: Extract only text for embeddings
doc_texts = [d["text"] for d in cricketers_docs]

docs_embeddings = embeddings.embed_documents(doc_texts)
query_embedding = embeddings.embed_query(query)

scores  = cosine_similarity([query_embedding], docs_embeddings)[0]

index , score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]

print(query)
print(cricketers_docs[index])
print("Similarity score is: ",score)