from typing import List, Optional
from pydantic import BaseModel
from app.schemas.color_semibot_schema import ColorOut, ColorCreate


class SemibotBase(BaseModel):
    name: str
    image: str
    description: Optional[str]


class SemibotCreate(SemibotBase):
    colors: List[ColorCreate] = []


class SemibotOut(SemibotBase):
    id: int
    colors: List[ColorOut]

    class Config:
        orm_mode = True
