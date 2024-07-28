from pydantic import BaseModel

class Image(BaseModel):
    id: int
    url: str
    tags: set

    class Config:
        orm_mode = True