from datetime import date
import datetime
import sys
from  database import session #データベースの接続
from  table_aqua import Attendnum #テーブル定義

args = sys.argv

#引数の格納
d = args[1]
a = int(args[2])
k = int(args[3])

#連番
s = session.query(Attendnum).filter_by(entry_date = d).count()+1 #executer

#追加するデータ
aqua = Attendnum(
    entry_date = d,
    seq =  s,
    adult = a,
    child = k
)

#INSERT
session.add(aqua)
#コミット
session.commit()