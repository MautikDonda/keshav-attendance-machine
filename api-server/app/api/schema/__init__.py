from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SystemDetails(BaseModel):
    machine_id: str
    machine_name: str
    time: datetime
    mode: str


class UpdateMachineName(BaseModel):
    machine_name: str
    ipaddress: str
    mode: str


class SwipeCard(BaseModel):
    card_number: str


class SwipeCardResponse(BaseModel):
    id: int
    card_number: str
    swipe_time: datetime
    machine_name: str
    user_id: str | None
    user_display_id: str | None
    user_name: str | None


class SyncUpAPISchema(BaseModel):
    url: str
    method: str
