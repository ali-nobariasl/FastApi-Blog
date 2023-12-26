from fastapi import FastAPI

from database import models
from database.database import engine

app = FastAPI()

@app.get('/')
def get_home():
    return {
        'message': 'this is my home page',
    }
    
    
    
models.Base.metadata.create_all(engine)