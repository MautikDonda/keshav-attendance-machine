from peewee import SqliteDatabase

from app.util import config

database = SqliteDatabase(config.get_db_path)
