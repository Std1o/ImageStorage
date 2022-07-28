from fastapi import FastAPI
from image_storage.api import router

app = FastAPI()
app.include_router(router)