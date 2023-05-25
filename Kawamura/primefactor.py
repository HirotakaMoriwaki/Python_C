import sys
args = sys.argv

input1 = int(args[1])
list_1 = []

i = 2

while i != input1:
    if input1 % i == 0:
        input1 = input1 // i
        list_1.append(i) 
    if input1 % i != 0:
        i = i + 1

list_1.append(i)       
print(list_1)