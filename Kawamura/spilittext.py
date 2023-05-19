import sys
args = sys.argv

input1 = args[1] 
input2 = args[2]

words = input1.split()

print(words[int(input2)-1], end="")