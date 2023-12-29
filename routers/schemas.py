from pydantic import BaseModel
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


# schema 
## we recieve user request
### user request contains all the information we need to create a new user


# model 
# database User
## conver from information we received to the database
### all the information of schema and all the process we nedd


# Database
# after creating a new user we send user response

##
## cerate user ---> user request ---> database user ---> create user in database
## --> user response