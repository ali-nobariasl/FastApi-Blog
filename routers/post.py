from fastapi import APIRouter, Depends , File, UploadFile
from sqlalchemy.orm.session import Session
import random
import string

from database import db_post , database
from routers.schemas import PostBase , PostDisplay

router = APIRouter(prefix='/post', tags=['post'])




@router.post('/', )
def create(request:PostBase, db:Session=Depends(database.get_db)):
    return db_post.create(db, request)


@router.get('/all')
def get_all_posts( db:Session=Depends(database.get_db)):
    return db_post.get_all(db)

@router.delete('/delete/{id}')
def delete_post( id:int , db:Session=Depends(database.get_db)):
    return db_post.delete_post(db, id)


@router.post('/image')
def upload_image(image:UploadFile= File(...) ):
    letter = string.ascii_letters
    rand_string = ''.join(random.choice(letter) for i in range(6))
    new = f'_{rand_string}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'
    
    with open(path, 'w+b') as f:
        shutil.copyfileobj(image.file, f)
        
    return {'filename': path}