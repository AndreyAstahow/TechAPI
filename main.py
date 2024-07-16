from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from random import randint, sample
from dotenv import load_dotenv

from schema import Image as SchemaImage
from models import ImageInfo as ModelImageInfo

import uvicorn
import os

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

def tags():
    all_tags = ['animal', 'cars', 'tech', 'посуда', 'млекопитающие', 'одежда', 'мебель', 'пингвин', 'лошадь', 'программа', 'искусство', 'стол', 'стул', 'дед мороз', 'праздник', 'деньги']
    return sample(all_tags, randint(0, 4))

@app.post('/image/')
def load_image(image: SchemaImage):
    image_tags = tags()
    db_image = ModelImageInfo(url = image.url, tags = image_tags)
    db.session.add(db_image)
    db.session.commit()
    return db_image

@app.get('/images/')
def get_image():
    image = db.session.query(ModelImageInfo).all()
    return image

@app.get('/image/')
def get_image_id(id: int):
    image = db.session.query(ModelImageInfo).filter(ModelImageInfo.id == id).first()
    return image

@app.get('/image/by-tags/')
def get_url_by_tags(tags: str):
    image = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
    return image

@app.get('/image/by-tags-and-id/')
def get_image_by_tags_and_id(id: int, tags: str):
    image_dict = []
    image_id = db.session.query(ModelImageInfo).filter(ModelImageInfo.id == id).all()
    image_tags = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
    image_dict.append(image_id)
    image_dict.append(image_tags)
    return image_dict

@app.get('/image/id-by-tags/')
def get_id_by_tags(tags: str):
    image_2 = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags.ilike(f"%{tags}%")).all()
    return image_2

if __name__ == '__main__':
    uvicorn.run(app)