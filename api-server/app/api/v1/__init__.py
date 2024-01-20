from fastapi import APIRouter

from app.api.v1 import system, attendance, sync_up, external_user

router = APIRouter(prefix="/v1")
router.include_router(system.router)
router.include_router(attendance.router)
router.include_router(sync_up.router)
router.include_router(external_user.router)
