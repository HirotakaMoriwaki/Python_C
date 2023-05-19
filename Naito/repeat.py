#100を超えるかどうかを判定するプログラム
import sys
#判定フラグ
hantei = True
#合計を計算する変数
sum=0
#変数に代入
c = sys.argv
kazu = int(c[1])

#判定コード
while hantei:
    sum += kazu
    #sumが100の時
    if (sum == 100):
        print("Just 100!",end="")
        hantei = False 
    #sumが100を超える時
    elif (sum > 100):
        print("Over!",end="")
        hantei = False