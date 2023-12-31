from datetime import datetime
import uuid
from peewee import *

from app import db


class BaseModel(Model):
    class Meta:
        database = db.database


class System(BaseModel):
    id = AutoField()
    key = CharField(null=False, unique=True)
    value = CharField(null=False)


from app.util.helpers import get_machine_name


class Attendance(BaseModel):
    id = AutoField()
    card_number = CharField()
    swipe_time = DateTimeField(default=datetime.now)
    machine_name = CharField(null=False, default=get_machine_name())


def create_tables():
    with db.database:
        db.database.create_tables([System])
        db.database.create_tables([Attendance])
        with db.database.atomic():
            for key, value in _default_system().items():
                if not System.select(System.value).where(System.key == key):
                    System.create(key=key, value=value)


def _default_system():
    return {
        'mode': 'Sabha',
        'machine_name': 'N/A',
        'machine_id': ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                                for elements in range(0, 2 * 6, 2)][::-1])
    }
