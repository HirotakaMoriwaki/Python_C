import sys
args = sys.argv

input1 = args[1] 
input2 = args[2] 
input3 = args[3]

if int(input1) >= 70 and int(input2) >= 70 and int(input3) >= 70 : #70以上なら合格
    print("合格", end="")
elif int(input1) < 50 or int(input2) < 50 or int(input3) < 50 : #どれか50未満か
    print("不合格", end="")
elif int(input1) + int(input2) + int(input3) >= 220 : #合計220以上かどうか
    print("合格", end="")
else :
    print("不合格", end="")
