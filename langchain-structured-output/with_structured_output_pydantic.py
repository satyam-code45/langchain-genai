from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

#schema
class Review(BaseModel):

    key_themes: list[str]  = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A breif summary of the review")
    sentiments: Literal["Positive", "Negative"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list." )
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list." )
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer.")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The Samsung Galaxy S24 Ultra continues to dominate the flagship market with its powerful hardware and refined design. Featuring a strong titanium frame and a large 6.8-inch Dynamic AMOLED 2X display, it delivers exceptional brightness, colors, and outdoor visibility. The Snapdragon 8 Gen 3 ensures blazing-fast performance for gaming, multitasking, and AI-powered features in One UI 6.1.

Its camera system is one of the most versatile available, with a 200MP main lens and an improved 5× optical zoom that produces sharp results even at long range. Battery life is solid thanks to a 5000 mAh cell, easily lasting a full day. Samsung also promises 7 years of updates, making it a reliable long-term choice.

However, the S24 Ultra isn’t perfect. It’s large and heavy, and charging speeds lag behind some competitors. The improvements over the S23 Ultra are mostly incremental. Still, with its superb display, performance, zoom capabilities, and S Pen support, the Galaxy S24 Ultra stands as one of the most complete premium smartphones available today.

Pros:

Stunning and ultra-bright AMOLED display

Powerful Snapdragon 8 Gen 3 performance

Excellent camera system with strong zoom

7 years of OS and security updates

Cons:

Expensive flagship pricing

Bulky and heavy design

Charging speeds not class-leading

Minor upgrade for S23 Ultra users""")

print(result)