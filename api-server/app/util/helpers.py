from app.db import get_cursor


def get_machine_name():
    machine_name_cursor = get_cursor()
    machine_name = machine_name_cursor.execute(
        "SELECT key, value FROM system where key='mode' or key='machine_name' order by key desc"
    ).fetchall()
    resp = []
    for item in machine_name:
        resp.append(item[1])
    return '-'.join(resp)
