# 引数受け取り
import sys
args = sys.argv
# 変数に格納

input1 = args[1]
input2 = args[2]
input3 = args[3]
"""
#int型に変換
num1 = int(input1)
num2 = int(input2)
num3 = int(input3)
"""
int(input1)
int(input2)
int(input3)

# 合計
sum = input1 + input2 + input3
# 出力
print(sum, end="")