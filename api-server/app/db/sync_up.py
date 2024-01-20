from app.db import get_cursor


def set_sys_key(key: str, value: str) -> None:
    is_key_exists = get_cursor().execute("SELECT * FROM system WHERE key=?", (key,))
    if len(is_key_exists.fetchall()) > 0:
        is_key_exists.close()
        get_cursor().execute("update system set value=? where key=?", (key, value, )).connection.commit()
    else:
        get_cursor().execute("insert into system (key, value) values (?, ?)", (key, value)).connection.commit()


def sync_up_settings_from_db():
    resp = {}
    data = get_cursor().execute("select key, value from system")
    for system in data:
        resp[system[0]] = system[1]
    return resp
