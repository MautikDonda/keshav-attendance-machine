from datetime import datetime

from app.db import database
from app.db.models import Attendance
from app.util import logger


def add_attendance_record(card_number: str) -> int:
    logger.logger.debug(f"ADD CARD NUMBER: {card_number}")
    try:
        with database.atomic():
            model = Attendance.create(card_number=card_number)
        return model.id
    except Exception as e:
        logger.logger.error(f"FAILED TO ADD CARD NUMBER: {card_number}")
        logger.logger.info(e)


def get_all_records(from_date: datetime | None = None, to_date: datetime | None = None):
    logger.logger.debug(f"GET ALL RECORDS")
    return [model for model in Attendance.select()]


def delete_all_records():
    logger.logger.debug(f"Start: DELETE ALL RECORDS")
    with database.atomic():
        Attendance.delete().execute()
    logger.logger.debug("End: DELETED ALL RECORDS")
