import uvicorn
from settings import settings


def main():
    uvicorn.run('image_storage.app:app',
                host=settings.server_host,
                port=settings.server_port,
                reload=True)


if __name__ == "__main__":
    main()