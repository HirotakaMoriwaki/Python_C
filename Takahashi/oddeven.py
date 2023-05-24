import sys
args = sys.argv

num = args[1]

if int(num) % 2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")