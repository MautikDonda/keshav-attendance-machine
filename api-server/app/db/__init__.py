import sqlite3

from app.util import config

database = sqlite3.connect(config.get_db_path, check_same_thread=False)


def get_cursor():
    return database.cursor()
