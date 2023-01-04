from pydantic import BaseModel
from typing import Union


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Token(OurBaseModel):
    access_token: str
    token_type: str

class TokenData(OurBaseModel):
    email: Union[str, None] = None
