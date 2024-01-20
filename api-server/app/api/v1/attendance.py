from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response, JSONResponse

from app.api.schema import SwipeCard, SwipeCardResponse
from app.db import attendance

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.get("", response_model=list[SwipeCardResponse])
def fetch_all_records():
    return attendance.get_all_records()


@router.get("/download")
def download_attendance_records(from_date: datetime, to_date: datetime):
    resp = attendance.get_all_records(from_date, to_date)
    headers = "UserId, UserDisplayId, UserName, CardNumber, Swipe Time, Machine Name"
    content = headers + '\n'
    for record in resp:
        content += (f"{record.user_id}, {record.user_display_id}, {record.user_name}, {record.card_number}, "
                    f"{record.swipe_time}, {record.machine_name}\n")
    response = Response(content=content.encode('utf8'), status_code=200)
    response.headers["Content-Disposition"] = (f"attachment; filename=Attendance_Report_{from_date.date().isoformat()}"
                                               f"_to_{to_date.date().isoformat()}.csv")
    response.headers["Content-Type"] = "application/octet-stream"
    return response


@router.delete("")
def delete_all_swipe_records():
    attendance.delete_all_records()
    return {"message": "All records deleted"}


@router.post("/swipe", status_code=201, response_model=SwipeCardResponse)
def swipe_card(data: SwipeCard):
    resp = attendance.add_attendance_record(data.card_number)
    if resp is not None:
        return resp
    return JSONResponse(status_code=500, content=f"Failed to process the request")
