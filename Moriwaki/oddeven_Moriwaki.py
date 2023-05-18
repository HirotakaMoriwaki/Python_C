###入力を受け取る###
import sys
num = int(sys.argv[1])

###偶奇判定###
if num % 2 == 0:
    print("偶数", end = "")
else:
    print("奇数", end = "")