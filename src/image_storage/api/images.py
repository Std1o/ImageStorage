from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
import shutil
from pathlib import Path
import os
import re


router = APIRouter(prefix='/images')

@router.get('/{image_name}')
def get_image(image_name: str):
    return FileResponse(f"../../images/{image_name}".encode('utf-8').decode('utf-8'))

@router.post("/uploadfile/")
async def create_upload_file(upload_file: UploadFile):
    try:
        with open(f"../../images/{upload_file.filename}".encode('utf-8'), "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
    ip_config = os.popen('ifconfig | grep "inet " | grep -v 127.0.0.1').readline().replace(" ", "")
    ip = re.search('inet(.*)netmask', ip_config)
    print(ip.group(1))
    return f"http://{ip.group(1)}/images/{upload_file.filename}"
