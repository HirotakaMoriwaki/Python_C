import sys
args = sys.argv

# 第二引数をtext、第三引数をnumに代入
text = args[1]
num = int(args[2])

# textを空白で区切り、text2に代入
text2 = text.split()

# text2のインデックス番号numの値を出力
print(text2[num-1],end="")