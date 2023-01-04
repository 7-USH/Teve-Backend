from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Fav(OurBaseModel):
    stream_link : str
    category: str
    channel_name: str