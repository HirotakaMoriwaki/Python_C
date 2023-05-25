import sys #sheep sleep
args = sys.argv

input1 = args[1] 
with open("../files/sheep.txt", mode="w", encoding="utf-8") as f:
    for i in range(1,int(input1) + 1) :
        print("ひつじが" + str(i) + "匹")
        f.write("ひつじが" + str(i) + "匹\n")