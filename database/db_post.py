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


def update(id:int,request:PostBase, db: Session):
    user = db.query(DbPost).filter(DbPost.id == id).first()
    if user:
        user.image_url = request.image_url
        user.title = request.title
        user.content = request.content
        user.creator = request.creator
        user.timestamp = datetime.datetime.now()
        
        db.commit()
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the user with {id} is not found')

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
    