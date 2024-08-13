from fastapi_sqlalchemy import db
from random import randint, sample

from database.schema import Image as SchemaImage
from database.models import ImageInfo as ModelImageInfo
from database.models import ImageTest as ModelImageTest

def tags():
    all_tags = ['animal', 'cars', 'tech', 'посуда', 'млекопитающие', 'одежда', 'мебель', 'пингвин', 'лошадь', 'программа', 'искусство', 'стол', 'стул', 'дед мороз', 'праздник', 'деньги']
    return sample(all_tags, randint(0, 4))

def tags_test():
    all_tags = ['кот', 'котячий ус', 'кот на лежанке', 'кот гуляет', 'кот сидит', 'собака', 'собака гуляет', 'собака ест', 'собака играет', 'еж несет яблоко', 'рыжий кот', 'мышка ест']
    return sample(all_tags, randint(0, 3))

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
        image = db.session.query(ModelImageInfo).filter(ModelImageInfo.tags.ilike(f'%{tags}%')).first()
        return image
    
    def load_image(image: SchemaImage):
        image_tags = tags()
        db_image = ModelImageInfo(url = image.url, tags = image_tags)
        db.session.add(db_image)
        db.session.commit()
        return db_image
    
    def load_test(image: SchemaImage):
        image_tags = tags_test()
        db_image = ModelImageTest(url = image.url, tags = image_tags)
        db.session.add(db_image)
        db.session.commit()
        return db_image
    
    def images_test():
        images = db.session.query(ModelImageTest).all()
        return images
    
    def get_id_by_tags_test(tags: str):
        image = db.session.query(ModelImageTest).filter(ModelImageTest.tags.ilike(f'%{tags}%')).first()
        return image
    
    def load_data(image: SchemaImage):
        count = 6
        while count <= 10000000:
            image_tags = tags_test()
            db_image = ModelImageTest(url = f'http://{count}.com', tags = image_tags)
            db.session.add(db_image)
            db.session.commit()
            count += 1