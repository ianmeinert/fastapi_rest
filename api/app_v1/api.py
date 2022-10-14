from fastapi import APIRouter

from api.app_v1.endpoints import orm, edi

api_router = APIRouter()
api_router.include_router(orm.router, prefix="/orm", tags=["orm"])
api_router.include_router(edi.router, prefix="/edi", tags=["edi"])
