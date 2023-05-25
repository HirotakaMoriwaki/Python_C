from  database import session #データベースの接続
from  tables import Holiday #テーブル定義
from datetime import date

holiday = session.query(Holiday).filter_by(holi_date=date(2024,1,1)).first()


holiday.holi_text = "元旦"

session.add(holiday)
session.commit()