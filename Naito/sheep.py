#引数分羊の数を数えるプログラム
import sys

args = sys.argv
#引数を変数に代入
count = int(args[1])

for i in range(1,count+1):
    print("ひつじが"+str(i)+"匹")