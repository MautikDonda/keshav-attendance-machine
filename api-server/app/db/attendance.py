from datetime import datetime

from app.api.schema import SwipeCardResponse
from app.db import get_cursor
from app.util import logger
from app.util.helpers import get_machine_name


def add_attendance_record(card_number: str) -> SwipeCardResponse:
    logger.logger.debug(f"ADD CARD NUMBER: {card_number}")
    try:
        user_cursor = get_cursor()
        user = user_cursor.execute(
            'SELECT id, display_id, first_name || " " || last_name name FROM externals_user WHERE card_number = ? '
            'order by id desc',
            (card_number,)).fetchone()
        user_cursor.close()
        machine_name = get_machine_name()
        new_attendance = get_cursor()
        new_attendance.execute(
            'INSERT INTO attendance (card_number, machine_name, user_id, swipe_time) VALUES (?, ?, ?, ?)',
            (card_number, machine_name, user[0] if user is not None else None, datetime.now()))
        new_attendance.connection.commit()
        new_attendance.close()
        return SwipeCardResponse(
            id=0,
            card_number=card_number,
            swipe_time=datetime.now(),
            machine_name=machine_name,
            user_id=user[0] if user is not None else None,
            user_display_id=user[1] if user is not None else None,
            user_name=user[2] if user is not None else None
        )
    except Exception as e:
        logger.logger.error(f"FAILED TO ADD CARD NUMBER: {card_number}")
        raise e


def get_all_records(from_date: datetime | None = None, to_date: datetime | None = None) -> list[SwipeCardResponse]:
    logger.logger.debug(f"GET ALL RECORDS")
    cursor = get_cursor()
    query = '''
    SELECT
       "t1"."id" "id",
       "t1"."card_number",
       "t1"."swipe_time",
       "t1"."machine_name",
       "t1"."user_id",
       "t2"."display_id" "user_display_id",
       "t2".first_name || " " || "t2".last_name name 
    FROM
        "attendance" "t1" 
    LEFT OUTER JOIN
      "externals_user" "t2" 
      ON ("t1"."user_id" = "t2"."id")
    '''
    sub_query = []
    param = []
    if from_date is not None:
        param.append(from_date)
        sub_query.append("t1.swipe_time > ?")
    if to_date is not None:
        param.append(to_date)
        sub_query.append("t1.swipe_time < ?")
    if len(sub_query) > 0:
        query += " WHERE " + " AND ".join(sub_query)
    cursor.execute(query, param)
    return [
        SwipeCardResponse(
            id=item[0],
            card_number=item[1],
            swipe_time=item[2],
            machine_name=item[3],
            user_id=item[4],
            user_display_id=item[5],
            user_name=item[6],
        ) for item in cursor.fetchall()
    ]


def delete_all_records():
    logger.logger.debug(f"Start: DELETE FROM ")
    cursor = get_cursor()
    cursor.execute("DELETE FROM attendance").connection.commit()
    cursor.close()
    logger.logger.debug("End: DELETED ALL RECORDS")
