# ３つの整数の足し算

import sys
args = sys.argv

# input変数に引数を代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

# 型変換＋足し算した値を出力
print(int(input1) + int(input2) + int(input3),end="")
