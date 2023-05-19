#英文とその英文の単語を取り出す
import sys

args=sys.argv
text = str(args[1])
n = int(args[2])

#英文からn番目の単語取り出し
text = text.split()
print(text[n-1],end="")