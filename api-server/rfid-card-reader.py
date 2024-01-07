# sql server connection string for local connection
from app.db import database
from app.db.attendance import add_attendance_record
from app.db.models import Attendance

# import pyodbc
# # Data Source=(LocalDb)\mssqllocaldb;Initial Catalog=APCERPDB;Integrated Security=True; Pooling=True
# cnxn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='(LocalDb)\mssqllocaldb', database='APCERPDB',
#                trusted_connection='yes')
#
# cursor = cnxn.cursor()
# c = cursor.execute("select * from [Attendance].[Sessions]")
# rows = c.fetchall()
# for row in rows:
#     print(row)0006390841


while True:
    card_id = input()
    database.connect(True)
    with database.atomic():
        model = Attendance.create(card_number=card_id)
    database.close()
    # if API is present, then call it.
