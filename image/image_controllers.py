from fastapi import APIRouter
from dotenv import load_dotenv

from database.schema import Image as SchemaImage

from .image_service import ImageService

load_dotenv('.env')

image = APIRouter()

@image.get('/images/')
def get_image():
    return ImageService.images()

@image.get('/image/')
def image_by_id(id: int):
    return ImageService.get_image_by_id(id)

@image.get('/image/by-tags/')
def image_by_tags(tags: str):
    return ImageService.get_image_by_tags(tags)

@image.get('/image/by-tags-and-id/')
def image_by_tags_and_id(id: int, tags: str):
    return ImageService.get_image_by_tags_and_id(id, tags)

@image.get('/image/id-by-tags/')
def get_id_by_tags(tags: str):
    return ImageService.get_id_by_tags(tags)

@image.post('/image/')
def load_image(image: SchemaImage):
    return ImageService.load_image(image)

@image.post('/image-test/')
def load_test(image: SchemaImage):
    return ImageService.load_test(image)

@image.get('/images-test/')
def images_test():
    return ImageService.images_test()

@image.get('/image/id-by-tags-test/')
def get_id_by_tags(tags: str):
    return ImageService.get_id_by_tags_test(tags)

@image.post('/load-data/')
def load_data(image: SchemaImage):
    return ImageService.load_data(image)