import sys
args = sys.argv

input1 = args[1] 
input2 = args[2]

words = input1.split() # 空白で区切る

print(words[int(input2)-1], end="") # 何番目の文字を指定する