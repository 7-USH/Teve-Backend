from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from teve.schemas import user_schema
from teve.models.models import User
from teve.config.hashing import Hash
from teve.config.authtoken import create_access_token

def create_user(db:Session,request:user_schema.User):
    new_user = User(email=request.email,password= Hash.bcrypt(request.password),name=request.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


def get_user(db:Session,id:int):
    user = db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'details of user not found')
    return user
