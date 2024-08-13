from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ImageInfo(Base):
    __tablename__ = 'image_info'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    tags = Column(String)


class ImageTest(Base):
    __tablename__ = 'image_test'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    tags = Column(String)