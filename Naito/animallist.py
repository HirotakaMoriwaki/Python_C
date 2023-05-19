#動物のリストに引数を挿入し並べ替えるプログラム
import sys

args = sys.argv
#変数に引数を代入
#場所
k = int(args[1])
#動物名
name = args[2]
if(k < 0 or k > 5):
    print("0から5の整数値を入力してください")
#動物のリスト
animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#挿入
animal.insert(k,name)

#最後の要素削除
del animal[len(animal)-1]

#リストを昇順に並べる
animal.sort(reverse=False)
print(animal,end="")