#計算
#sys:実行のコマンドの入力の際に変数に入れる中身を入力できる
import sys
args = sys.argv

#引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

result=int(input1)+int(input2)+int(input3)
#表示　end="":改行なし
print(result,end="")
