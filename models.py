from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class ImageInfo(Base):
    __tablename__ = 'image_info'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    tags = Column(String)