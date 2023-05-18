#教科の点数で合格を表示コード
import sys
args = sys.argv

#変数に代入
ma_p = int(args[1])
ja_p = int(args[2])
en_p = int(args[3])

#合計を求める
sam=ma_p+ja_p+en_p
#判定フラグ
hantei = False

if(ma_p < 50 or ja_p < 50 or en_p < 50):
    hantei = False
elif((ma_p >= 70 & ja_p >=70 & en_p >=70) or sam >=220):
    hantei = True

if hantei:
    print("合格",end="")
else:
    print("不合格",end="")