from app.db.attendance import add_attendance_record

while True:
    card_id = input()
    resp = add_attendance_record(card_id)
