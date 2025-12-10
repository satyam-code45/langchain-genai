from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
])

# Path of folder where THIS script lives
BASE_DIR = Path(__file__).resolve().parent

# Full path to chat_history.txt
history_file = BASE_DIR / "chat_history.txt"

print("Looking for file at:", history_file)  # debug

# Load chat history
chat_history = []

with open(history_file, "r") as f:
    chat_history = f.readlines()


prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})


print(prompt)