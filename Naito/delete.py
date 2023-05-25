from  database import session #データベースの接続
from  tables import Holiday #テーブル定義
from datetime import date

result = session.query(Holiday).filter_by(holi_date=date(2024,1,1)).delete()

session.commit()