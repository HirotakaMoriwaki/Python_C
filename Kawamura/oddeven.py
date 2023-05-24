import sys
args = sys.argv

#引数を変数に代入
input = args[1]

if int(input)%2 == 0 :
    print("偶数", end="")
else:
    print("奇数", end="")