import sys
args = sys.argv

input1 = int(args[1])
input2 = args[2]

list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

list.insert(input1,input2)
del list[-1]
list.sort()
print(args[0])