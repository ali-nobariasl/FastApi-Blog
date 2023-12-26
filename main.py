from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from database import model
from database.database import engine
from routers import post


app = FastAPI()
app.include_router(post.router)



@app.get('/')
def get_home():
    return {'message': 'this is my home page',}
    
    
model.Base.metadata.create_all(engine)
app.mount('/images',StaticFiles(directory='images'), name='images')


## CORS allows us to have access to our local API
## from local endPOint

origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ['*']
)