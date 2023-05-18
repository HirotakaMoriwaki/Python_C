#名前の出力
#sys:実行のコマンドの入力の際に変数に入れる中身を入力できる
import sys
args = sys.argv

#引数を変数に代入
name = args[1]

#表示　end="":改行なし
print("Hello "+name+" !", end="")

