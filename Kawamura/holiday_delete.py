from datetime import date
from database import session
from tables import Holiday

# 指定した日を削除
result = session.query(Holiday).filter_by(holi_date=date(2014, 1, 1)).delete()

session.commit()