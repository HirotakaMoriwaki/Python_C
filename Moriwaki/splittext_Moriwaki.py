import sys

list_word = list(sys.argv[1].split())
num = int(sys.argv[2])

print(list_word[num - 1], end = "")