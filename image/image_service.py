from fastapi_sqlalchemy import db
from random import randint, sample

from database.schema import Image as SchemaImage
from database.models import ImageInfo as ModelImageInfo

def tags():
    all_tags = ['animal', 'cars', 'tech', 'посуда', 'млекопитающие', 'одежда', 'мебель', 'пингвин', 'лошадь', 'программа', 'искусство', 'стол', 'стул', 'дед мороз', 'праздник', 'деньги']
    return sample(all_tags, randint(0, 4))

class ImageService():
    def images():
        images = db.session.query(ModelImageInfo).all()
        return images

    def get_image_by_id(id: int):
        image = db.session.query(ModelImageInfo).filter(ModelImageInfo.id == id).first()
        return image
    
    def get_image_by_tags(tags: str):
        image = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
        return image
    
    def get_image_by_tags_and_id(id: int, tags: str):
        image_dict = []
        image_id = db.session.query(ModelImageInfo).filter(ModelImageInfo.id == id).all()
        image_tags = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags == tags).all()
        image_dict.append(image_id)
        image_dict.append(image_tags)
        return image_dict
    
    def get_id_by_tags(tags: str):
        image = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags.ilike(f'%{tags}%')).all()
        return image
    
    def load_image(image: SchemaImage):
        image_tags = tags()
        db_image = ModelImageInfo(url = image.url, tags = image_tags)
        db.session.add(db_image)
        db.session.commit()
        return db_image