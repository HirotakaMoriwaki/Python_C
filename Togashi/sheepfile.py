import sys
args = sys.argv
# 引数をint型に変換
num = int(args[1])+1
'''
with open("../../files/sheep.txt", mode = "w",encoding = "utf-8") as f:
    for i in range(1,num):
        f.write("ひつじが"+str(i)+"匹\n")'''

a_file = open("../../files/sheep.txt", mode = "a",encoding = "utf-8")
try:
    for i in range(1,num):
        a_file.write("ひつじが"+str(i)+"匹\n")
finally:
    a_file.close()