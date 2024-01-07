import json

from app.api.schema import SyncUpAPISchema
from app.db import database
from app.db.models import System


def set_live_swipe_api(data: SyncUpAPISchema):
    with database.atomic():
        if not System.select().where(System.key == "live_swipe"):
            System.create(key="live-swipe", value=data.model_dump_json())
        else:
            System.update(value=data.model_dump_json()).where(System.key == "live_swipe").execute()


def sync_up_settings_from_db():
    resp = {}
    with database.atomic():
        for system in System.select():
            if system.key in ("live-swipe", 'server_time', "attendance_sync"):
                resp[system.key] = json.loads(system.value)
    return resp


def set_server_time_api(data: SyncUpAPISchema):
    with database.atomic():
        if not System.select().where(System.key == "server_time"):
            System.create(key="server_time", value=data.model_dump_json())
        else:
            System.update(value=data.model_dump_json()).where(System.key == "server_time").execute()


def set_attendance_sync_api(data: SyncUpAPISchema):
    with database.atomic():
        if not System.select().where(System.key == "attendance_sync"):
            System.create(key="attendance_sync", value=data.model_dump_json())
        else:
            System.update(value=data.model_dump_json()).where(System.key == "attendance_sync").execute()
