from fastapi import APIRouter

from app.api.schema import SwipeCard, SwipeCardResponse
from app.db.attendance import add_attendance_record, get_all_records, delete_all_records

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.get("", response_model=list[SwipeCardResponse])
def fetch_all_records():
    resp = get_all_records()
    return resp


@router.delete("")
def delete_all_swipe_records():
    delete_all_records()
    return {"message": "All records deleted"}


@router.post("/swipe", status_code=201, response_model=int)
def swipe_card(data: SwipeCard):
    return add_attendance_record(data.card_number)
