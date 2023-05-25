import sys
import os

count = int(sys.argv[1])

PATH = os.path.join("..","files","sheep.txt")
print(PATH)

txt = open(PATH, mode = "w", encoding = "utf-8")

for i in range(count):
    txt.write("ひつじが" + str(i+1) + "匹" + "\n")


txt.close()