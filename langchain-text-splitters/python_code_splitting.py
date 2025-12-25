from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = ''''
class SimpleTextSplitter:
    def __init__(self, chunk_size=100, chunk_overlap=20):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str):
        """
        Splits text into overlapping chunks.
        """
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)

            # Move start forward with overlap
            start = end - self.chunk_overlap

        return chunks


# ----------------- TEST -----------------

if __name__ == "__main__":
    sample_text = (
        "Rohit Sharma is one of India's finest cricketers. "
        "He is known for his elegant batting style and leadership. "
        "He holds the record for the highest individual score in ODI cricket. "
        "Rohit has also been very successful as a captain."
    )

    splitter = SimpleTextSplitter(chunk_size=50, chunk_overlap=10)
    chunks = splitter.split_text(sample_text)

    for i, chunk in enumerate(chunks, 1):
        print(f"\nChunk {i}:\n{chunk}")

'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(chunks[2])
print(len(chunks))