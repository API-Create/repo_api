from pydantic import BaseModel

class ColorBase(BaseModel):
    name: str
    image: str

class ColorCreate(ColorBase):
    pass

class ColorOut(ColorBase):
    id: int

    class Config:
        orm_mode = True
