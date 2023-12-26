from pydandtic import BaseModel
from datetime import datetime 


#info we received from API
class PostBase(BaseModel):
    image_url: str
    title : str
    content : str
    creator : str
  
# info we want to send  
class PostDisplay(BaseModel):
    id : int
    image_url: str
    title : str
    content : str
    creator : str
    timestamp: datetime
    class Config():
        orm_model = True
