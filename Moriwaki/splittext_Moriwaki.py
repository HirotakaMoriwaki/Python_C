import sys

###入力を受け取りwordリスト・数値としてそれぞれ格納
list_word = list(sys.argv[1].split())
num = int(sys.argv[2])

###指定されたインデックスの単語を出力
print(list_word[num - 1], end = "")