from sqlalchemy.orm.session import Session
from fastapi import HTTPException , status
import datetime

from routers.schemas import PostBase
from database.model import DbPost

def create(db: Session, request:PostBase):
    user = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator, 
        timestamp = datetime.datetime.now()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all(db:Session):
    users = db.query(DbPost).all()
    return users

def delete_post(db:Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if post:
        db.delete(post)
        db.commit()
        return 'Ok Baby'
        
    else:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post with this id is not found')
    