from sqlalchemy.orm.session import Session
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