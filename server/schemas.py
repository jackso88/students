import datetime
from typing import List

from pydantic import BaseModel


class PostRemoveItem(BaseModel):
    id: int

    class Config:
        orm_mode = True

