import pathlib

path = pathlib.Path(__file__).parent.parent.parent.resolve()
get_db_path = path.joinpath("attendance1.db")
