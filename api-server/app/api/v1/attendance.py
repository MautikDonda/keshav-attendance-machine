from datetime import datetime

from fastapi import APIRouter
from starlette.responses import FileResponse, Response

from app.api.schema import SwipeCard, SwipeCardResponse
from app.db.attendance import add_attendance_record, get_all_records, delete_all_records

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.get("", response_model=list[SwipeCardResponse])
def fetch_all_records():
    resp = get_all_records()
    return resp


@router.get("/download")
def download_attendance_records(from_date: datetime, to_date: datetime):
    resp = get_all_records(from_date, to_date)
    headers = "UserId, UserDisplayId, UserName, CardNumber, Swipe Time, Machine Name"
    response = Response(content=headers.encode('utf8'), status_code=200)
    response.headers["Content-Disposition"] = (f"attachment; filename=Attendance_Report_{from_date.date().isoformat()}"
                                               f"_to_{to_date.date().isoformat()}.csv")
    response.headers["Content-Type"] = "application/octet-stream"
    return response
    

@router.delete("")
def delete_all_swipe_records():
    delete_all_records()
    return {"message": "All records deleted"}


@router.post("/swipe", status_code=201, response_model=int)
def swipe_card(data: SwipeCard):
    return add_attendance_record(data.card_number)
