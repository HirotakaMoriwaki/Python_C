from datetime import date
import datetime
import sys

args = sys.argv

#引数の格納
d = args[1]
adult = int(args[2])
kid = int(args[3])

#料金格納 大人:price[0] 子供price[1]
price =[[2000,2400],[1200,1500]]

#平日か休日の判定
# 文字列型 → datetime型
d = datetime.datetime.strptime(d, "%Y%m%d")
hantei = d.strftime("%a")

#料金の表示
if(hantei == 'Sat' or hantei == 'Sun'):
    k = 1
    sum = (price[0][k]*adult)+(price[1][k]*kid)
else:
    k = 0
    sum = price[0][k]*adult+price[1][k]*kid

print(sum,end='')