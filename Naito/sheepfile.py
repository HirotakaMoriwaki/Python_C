#引数分羊の数を数えるプログラム
import sys

args = sys.argv
#引数を変数に代入
count = int(args[1])

with open("./Files/sheep.txt", "w") as f:
    for i in range(1,count+1):
        f.write("ひつじが"+str(i)+"匹\n")