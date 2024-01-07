from datetime import datetime

from app.api.schema import SystemDetails, UpdateMachineName
from app.db.models import System


def get_systems():
    model = SystemDetails(
        mode=System.select(System.value).where(System.key == 'mode')[0].value,
        time=datetime.now(),
        machine_id=System.select(System.value).where(System.key == 'machine_id')[0].value,
        machine_name=System.select(System.value).where(System.key == 'machine_name')[0].value
    )
    return model


def update_machine_info(data: UpdateMachineName):
    System.update(value=data.machine_name).where(System.key == 'machine_name').execute()
    System.update(value=data.mode).where(System.key == 'mode').execute()
    # Update IP
