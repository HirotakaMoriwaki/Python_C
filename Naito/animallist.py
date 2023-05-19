#動物のリストに引数を挿入し並べ替えるプログラム
import sys

args = sys.argv
#変数に引数を代入
#場所/動物名
k = int(args[1])
name = args[2]

#動物のリスト
animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#挿入
animal.insert(k,name)

#最後の要素削除
#del animal[len(animal)-1]#lenは１から
del animal[-1]

#リストを昇順に並べる
animal.sort(reverse=False)

print(animal,end="")