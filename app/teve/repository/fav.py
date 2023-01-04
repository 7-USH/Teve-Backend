from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from teve.database.database import get_db
from teve.models.models import User, Fav
from teve.schemas import fav_schema

def add_to_fav(current_user: str, request: fav_schema.Fav, db: Session = Depends(get_db)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User doesnt exist")
    try:
        user = db.query(User).filter(User.email == current_user).first()
        user_fav = Fav(stream_link=request.stream_link, category=request.category,
                    channel_name=request.channel_name, user_id=user.email)
        db.add(user_fav)
        db.commit()
        db.refresh(user_fav)
        return user_fav
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Detail already existed")

def get_user_favs(current_user:str ,db:Session=Depends(get_db)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User doesnt exist")
    favs = db.query(Fav).filter(Fav.user_id == current_user).all()
    return favs


def delete_user_favs(current_user: str, request: fav_schema.Fav, db: Session = Depends(get_db)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User doesnt exist")
    try:
        db.query(Fav).filter(Fav.user_id == current_user, Fav.stream_link == request.stream_link,
                         Fav.category == request.category).delete(synchronize_session=False)
        db.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Nothing to delete")
