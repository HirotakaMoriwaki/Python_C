from  database import session #データベースの接続
from  tables import Holiday #テーブル定義
from datetime import date

#追加するデータ
holiday = Holiday(
    holi_date = date(2024,1,1),
    holi_text = "お正月"
)
#INSERT
session.add(holiday)
#コミット
session.commit()