#東京駅からの距離を求めるプログラム
import sys 

args =sys.argv
#変数に駅を代入
start = args[1]
end = args[2]
dis ={
    "東京":0.00,
    "品川":6.78,
    "新横浜":25.54,
    "名古屋":342.02,
    "京都":476.31,
    "新大阪":515.35
}

try:
    print('{:.2f}'.format(abs(dis[end]-dis[start])),end='')
except KeyError:
    print("のぞみの停車駅を引数に設定してください",end="")
#print(round(abs(dis[end]-dis[start]),2),end='')
