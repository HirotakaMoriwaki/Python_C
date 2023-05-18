#入力を受け取る
import sys
num = sys.argv[1:4]

#配列内の型をintに
for i in range(len(num)):
    num[i] = int(num[i])

#配列内合計を出力
print(sum(num))