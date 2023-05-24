import sys
args = sys.argv

Math = args[1]
Japanese = args[2]
English = args[3]

if int(Math)>=70 and int(Japanese)>=70 and int(English)>=70:
    result = True
elif int(Math)+int(Japanese)+int(English)>=220 and (int(Math)>=50 and int(Japanese)>=50 and int(English)>=50):
    result = True
else:
    result = False

if result == True:
    print("合格",end="")
else:
    print("不合格",end="")