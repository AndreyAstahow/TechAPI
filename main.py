from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from image.image_controllers import image
from dotenv import load_dotenv

import uvicorn
import os

load_dotenv('.env')

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])
app.include_router(image)


if __name__ == "__main__":
    uvicorn.run(app)