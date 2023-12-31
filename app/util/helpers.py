from app.db import database
from app.db.models import System


def get_machine_name():
    with database.atomic():
        machine_name = System.select(System.value).where(System.key == 'mode')
    return machine_name
