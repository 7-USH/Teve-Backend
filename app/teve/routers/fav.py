from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from teve.schemas import fav_schema, user_schema
from teve.database.database import get_db
from teve.config.oauth2 import get_current_user
from teve.repository import fav
from typing import List


router = APIRouter(tags=["favourites"],prefix="/fav")


@router.get("/", response_model=List[fav_schema.Fav])
def get_all_fav(db: Session = Depends(get_db), current_user: user_schema.User = Depends(get_current_user)):
    return fav.get_user_favs(current_user=current_user, db=db)

@router.post("/add")
def add_to_fav(request:fav_schema.Fav,db:Session=Depends(get_db),current_user:user_schema.User=Depends(get_current_user)):
    return fav.add_to_fav(current_user=current_user,db=db,request=request)

@router.delete("/delete")
def delete_fav(request: fav_schema.Fav, db: Session = Depends(get_db), current_user: user_schema.User = Depends(get_current_user)):
    return fav.delete_user_favs(current_user=current_user,request=request,db=db)
