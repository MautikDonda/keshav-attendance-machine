import uuid

from app.db import get_cursor

_migration_1_base_tables = '''
create table if not exists main.attendance
(
    id           INTEGER  primary key AUTOINCREMENT,
    card_number  VARCHAR(255) not null,
    swipe_time   DATETIME     not null default CURRENT_TIMESTAMP,
    machine_name VARCHAR(255) not null,
    user_id      VARCHAR(255)
);

create table if not exists main.externals_user
(
    id          VARCHAR(255) not null primary key,
    first_name  VARCHAR(255) not null,
    last_name   VARCHAR(255) not null,
    display_id  VARCHAR(255) not null,
    card_number VARCHAR(255) not null
);

create table if not exists  main.system
(
    id    INTEGER      primary key AUTOINCREMENT,
    key   VARCHAR(255) not null,
    value VARCHAR(255) not null
);

create unique index if not exists system_key on system (key);
'''


def create_tables():
    get_cursor().executescript(_migration_1_base_tables).close()
    # dump machine default values
    for key, value in _default_system().items():
        get_cursor().execute("INSERT INTO system (key, value) VALUES (?,?)", (key, value)).close()


def _default_system():
    return {
        'mode': 'Sabha',
        'machine_name': 'N/A',
        'machine_id': ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                                for elements in range(0, 2 * 6, 2)][::-1])
    }
