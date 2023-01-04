from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class User(OurBaseModel):
    email:str
    password:str
    name: str

class UserView(OurBaseModel):
    email: str
    name:str
