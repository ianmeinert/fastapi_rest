from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from core.config import settings
from api.app_v1.api import api_router

MIDDLEWARE = [
    Middleware(CORSMiddleware,
               allow_origins=[
                   str(origin) for origin in settings.BACKEND_CORS_ORIGINS
                ],
               allow_credentials=True,
               allow_methods=['GET, POST'],
               allow_headers=["*"])
    ]

router = APIRouter()

api = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        contact={
            "name": "Ian Meinert",
        },
        openapi_tags=settings.TAGS_METADATA,
        docs_url="/documentation",
        redoc_url=None,
        middleware=MIDDLEWARE,
        openapi_url="/openapi.json"
    )


@router.get('/', name='home', status_code=200)
async def index():
    return {"message": "API is online"}

api.include_router(router)
api.include_router(api_router, prefix=settings.API_V1_STR, tags=["v1"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=api, host='localhost', port=8000)
