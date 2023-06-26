from sqlalchemy import Column, Integer, Text, Date, ARRAY
from config import Base

class Post(Base):
    __tablename__ ="posts"

    id = Column(Integer, primary_key=True, index=True)
    rubrics = Column(ARRAY(Text()), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)
