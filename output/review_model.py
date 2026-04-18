from pydantic import BaseModel,Field
from langchain_ollama import ChatOllama
from typing import Literal, TypedDict,Annotated,Optional
llm=ChatOllama(model=" phi3:mini")

class Review(BaseModel):
    key_themes:list[str]=Field(description="write all The Key Features")
    summary:str=Field(description="A brief Summary")
    sentiments:Literal["pos","neg"]=Field(description="Return Sentiment of The Review either negative oR positive")
    pros:list[str]=Field(default=None,description="write all The Pros")
    cons:list[str]=Field(default=None,description="Write All The Cons")
    

structured_model=llm.with_structured_output(Review)

result=structured_model.invoke("""The Apple iPhone 15 is a modern smartphone that combines premium design with strong performance. It features a sleek aluminum body and a bright OLED display that delivers sharp colors and smooth visuals while watching videos or browsing. Powered by the fast Apple A16 Bionic chip, the device runs applications quickly and handles multitasking efficiently, making it suitable for gaming and everyday tasks. The camera system captures detailed photos with accurate colors, and the portrait mode produces impressive background blur. Battery life is generally reliable for a full day of moderate usage, and the device also supports fast charging. However, the phone is quite expensive compared to many competitors, which may not fit every buyer’s budget. Some users might also feel that the base storage option is limited for heavy media usage. While the design is elegant and comfortable to hold, the charging speed is slower than several Android phones in the same price range. Additionally, customization options in the operating system are more restricted compared to some other smartphones. Overall, the phone delivers excellent performance, a high-quality camera, and a premium build, though its high price, limited customization, and relatively slower charging may be disadvantages for certain users.""")
print(result.model_dump_json())