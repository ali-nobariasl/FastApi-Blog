from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from database import db_post , database
from routers.schemas import PostBase , PostDisplay

router = APIRouter(prefix='/post', tags=['post'])




@router.post('/', )
def create(request:PostBase, db:Session=Depends(database.get_db)):
    return db_post.create(db, request)