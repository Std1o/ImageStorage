from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
import shutil
from pathlib import Path


router = APIRouter(prefix='/images')

@router.get('/{image_name}')
def get_image(image_name: str):
    return FileResponse(f"../../images/{image_name}.png")

@router.post("/uploadfile/")
async def create_upload_file(upload_file: UploadFile):
    destination = Path(f"../../images/{upload_file.filename}")
    print(destination.absolute())
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
    return {"filename": upload_file.filename}