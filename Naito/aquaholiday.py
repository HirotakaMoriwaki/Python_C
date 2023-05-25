from datetime import date
import datetime
import sys
from  database import session #データベースの接続
from  tables import Holiday #テーブル定義

args = sys.argv

#引数の格納
d = args[1]
adult = int(args[2])
kid = int(args[3])

#料金格納 大人:price[0] 子供price[1]
price =[[2000,2400],[1200,1500]]

# 平日か休日の判定
# 文字列型 → datetime型
d = datetime.datetime.strptime(d, "%Y%m%d")
hantei = d.strftime("%a")

#祝日の日にちをデータベースから取り出す
#全件取得の場合
holidaylist = session.query(Holiday).all()
d = d.date()#date型に

#祝日判定
for holi in holidaylist:
    d_h = holi.holi_date
    if(d == d_h):
        hantei = 'Holi'
print(hantei)
#料金の表示
if(hantei == 'Sat' or hantei == 'Sun' or hantei=='Holi'):
    k = 1
    sum = (price[0][k]*adult)+(price[1][k]*kid)
else:
    k = 0
    sum = price[0][k]*adult+price[1][k]*kid

print(sum,end='')