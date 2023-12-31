from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api.schema import SyncUpAPISchema
from app.db.sync_up import set_live_swipe_api, sync_up_settings_from_db, set_server_time_api, set_attendance_sync_api

router = APIRouter(prefix="/sync-up", tags=["Sync Up"])


@router.get("")
def sync_up_settings():
    return sync_up_settings_from_db()


@router.post("/live-swipe")
def live_swipe_api(url_data: SyncUpAPISchema):
    set_live_swipe_api(url_data)
    return JSONResponse("Success", status_code=201)


@router.post("/time")
def get_server_time(url_data: SyncUpAPISchema):
    set_server_time_api(url_data)
    return JSONResponse("Success", status_code=201)


@router.post("/attendance")
def get_server_time(url_data: SyncUpAPISchema):
    set_attendance_sync_api(url_data)
    return JSONResponse("Success", status_code=201)
