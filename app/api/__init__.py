from fastapi import APIRouter

from app.api.v1 import system

router = APIRouter(prefix="/api")
router.include_router(v1.router)
