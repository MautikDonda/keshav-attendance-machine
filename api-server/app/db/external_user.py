from app.api.schema import ExternalUser
from app.db import get_cursor


def get_users():
    cursor = get_cursor()
    cursor.execute('select id, display_id, first_name, last_name, card_number from externals_user')
    users = cursor.fetchall()
    cursor.close()
    return [ExternalUser(
        id=user[0],
        display_id=user[1],
        first_name=user[2],
        last_name=user[3],
        card_number=user[4]
    ) for user in users]


def get_user_by_id(uid: str):
    cursor = get_cursor()
    cursor.execute('select id, display_id, first_name, last_name, card_number from externals_user where id = ?', (uid,))
    user = cursor.fetchone()
    cursor.close()
    return ExternalUser(
        id=user[0],
        display_id=user[1],
        first_name=user[2],
        last_name=user[3],
        card_number=user[4]
    )


def add_user(user: ExternalUser) -> ExternalUser:
    cursor = get_cursor()
    cursor.execute('insert into externals_user (id, display_id, first_name, last_name, card_number) values (?,?,?,?,?)',
                   (user.id, user.display_id, user.first_name, user.last_name, user.card_number))
    cursor.connection.commit()
    cursor.close()
    return get_user_by_id(user.id)
