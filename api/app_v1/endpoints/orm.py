from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api import deps
from models import imsw_models

router = APIRouter()


@router.get("/test-first-of-all", tags=["test-first-of-all"], status_code=200)
async def First_from_full_ORM_model_set(db: Session = Depends(deps.get_db)):
    firstOfAll = (
        db.query(imsw_models.t_ViewRestricted)
        .order_by(imsw_models.t_ViewRestricted.columns.SomeDateTime.desc())
        .all()
    )

    return firstOfAll


@router.get("/test-first", tags=["test-first"], status_code=200)
async def First_record_from_ORM_model_set(db: Session = Depends(deps.get_db)):
    first = (
        db.query(imsw_models.t_ViewRestricted)
        .order_by(imsw_models.t_ViewRestricted.columns.SomeDateTime.desc())
        .first()
    )

    return first


@router.get("/test-filtered", tags=["test-filtered"], status_code=200)
async def Filtered_from_ORM_model_set(db: Session = Depends(deps.get_db)):
    filtered = (
        db.query(imsw_models.t_ViewRestricted)
        .filter(imsw_models.t_ViewRestricted.columns.SomeDateTime > "2022-03-01")
        .order_by(imsw_models.t_ViewRestricted.columns.SomeDateTime.desc())
        .first()
    )

    return filtered
