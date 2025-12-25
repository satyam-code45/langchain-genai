from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    chunk_size=100, chunk_overlap=0, separator=""
)

document = """
Rohit Sharma is one of India’s most accomplished cricketers, known for his effortless batting and elegant stroke play. Nicknamed the “Hitman,” he holds the record for the highest individual score in ODIs (264 runs) and is the only player to score three double centuries in the format.

As an opening batter, Rohit excels at building innings, combining patience with explosive power. He is also a highly successful captain, having led teams to multiple IPL titles and guiding India with calm leadership and sharp cricketing intelligence.

With consistency across formats, exceptional timing, and a knack for big-match performances, Rohit Sharma has cemented his place as one of the greats of modern cricket.
"""

texts = text_splitter.split_text(document)

print(texts)