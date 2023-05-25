import sys
args = sys.argv
# 文字列を格納
eibun = args[1]
# 何番目かを格納
num = int(args[2])
num = num - 1
# 空白で分割してリストにいれる
tango = list(eibun.split())
# リスト「tango」のnum番目を出力
print(tango[num], end="")
