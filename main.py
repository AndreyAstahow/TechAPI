from fastapi import FastAPI
from random import randint
from io import BytesIO
from PIL import Image

import uvicorn
import requests

app = FastAPI()

@app.get('/url')
async def test(url: str):
    response = requests.get(url)
    img_data = response.content
    image = Image.open(BytesIO(img_data))
    width, height = image.size
    info = { 'width': width, 'height': height}
    return {
        'url' : f'{url}',
        'id' : randint(100000, 999999),
        'info' : info,
    }

if __name__ == '__main__':
    uvicorn.run(app)