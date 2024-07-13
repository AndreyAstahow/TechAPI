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
    tags = random.sample(all_tags, random.randint(0, 4))
    return tags


@app.post('/load_image/')
def load_image(image: SchemaImage):
    image_tags = tags()
    db_image = ModelImageInfo(url = image.url, tags = image_tags)
    db.session.add(db_image)
    db.session.commit()
    return db_image

@app.get('/get_image/')
def get_image():
    image = db.session.query(ModelImageInfo).all()
    return image

@app.get('/get_image/{id}')
def get_image_id(id: int):
    image = db.session.query(ModelImageInfo).filter(ModelImageInfo.id == id).first()
    return image

@app.get('/get_url_by_tags/')
def get_url_by_tags(tags: str):
    image = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
    return image

@app.get('/get_image_by_tags_and_id/')
def get_image_by_tags_and_id(id: int, tags: str):
    image_dict = []
    image_id = db.session.query(ModelImageInfo).filter(ModelImageInfo.id == id).all()
    image_tags = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
    image_dict.append(image_id)
    image_dict.append(image_tags)
    return image_dict

@app.get('/get_id_by_tags/')
def get_id_by_tags(tags: str):
    image = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
    return image

if __name__ == '__main__':
    uvicorn.run(app)