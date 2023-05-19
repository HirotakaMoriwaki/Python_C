#嫌いな食べ物の表示
#sys:実行のコマンドの入力の際に変数に入れる中身を入力できる
import sys
args = sys.argv

food = args[1]

print("I don't like",food,end="")