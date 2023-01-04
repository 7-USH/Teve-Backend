from pydantic import BaseModel
from typing import Union


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Login(OurBaseModel):
    username: str
    password: str
