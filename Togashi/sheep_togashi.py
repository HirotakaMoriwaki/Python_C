import sys
args = sys.argv
# 引数をint型に変換
num = int(args[1])+1
for i in range(1,num):
    print("ひつじが"+str(i)+"匹")