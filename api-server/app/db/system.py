from datetime import datetime

from app.api.schema import SystemDetails, UpdateMachineName
from app.db import get_cursor


def get_systems():
    cursor = get_cursor()
    cursor.execute("select key, value from system")
    systems = cursor.fetchall()
    mode = ''
    machine_name = ''
    machine_id = ''
    for system in systems:
        if system[0] == 'mode':
            mode = system[1]
        elif system[0] == 'machine_name':
            machine_name = system[1]
        elif systems[0] == 'machine_id':
            machine_id = system[1]

    model = SystemDetails(
        mode=mode,
        time=datetime.now(),
        machine_id=machine_id,
        machine_name=machine_name
    )
    return model


def update_machine_info(data: UpdateMachineName):
    cursor = get_cursor()
    cursor.execute("update system set value = ? where key = ?", (data.machine_name, 'machine_name'))
    cursor.execute("update system set value = ? where key = ?", (data.mode, 'mode'))
    # Update IP
    cursor.close()
    return get_systems()
