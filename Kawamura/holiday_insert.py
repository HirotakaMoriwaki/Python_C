from datetime import date
from database import session
from tables import Holiday

# 指定した日を追記
holiday = Holiday(
    holi_date = date(2024, 1, 1),
    holi_text = "お正月"
)
session.add(holiday)

session.commit()