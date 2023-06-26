from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
import datetime

class PostRemoveItem(BaseModel):
    id: int

    class Config:
        orm_mode = True

class Post(PostRemoveItem):
    text: str
    rubrics: List[str]
    created_date: datetime.datetime

    class Config:
        orm_mode = True
