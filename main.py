from fastapi import FastAPI

from database import model
from database.database import engine
from routers import post


app = FastAPI()
app.include_router(post.router)



@app.get('/')
def get_home():
    return {'message': 'this is my home page',}
    
    
model.Base.metadata.create_all(engine)
