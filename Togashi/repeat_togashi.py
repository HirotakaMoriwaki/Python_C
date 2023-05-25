import sys
args = sys.argv
# 引数をint型に変換
num = int(args[1])
# 合計を入れる変数は最初0にする
sum = 0
# 100未満の場合は続ける
while sum < 100 :    
    sum += num
    if sum == 100:
        print("Just 100!",end="")
        break
    elif sum > 100:
        print("Over!",end="")
        break
    else:
        continue