import sys
###入力を受け取り番号と動物名を受け取る
index = int(sys.argv[1])
name = sys.argv[2]

list_animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]

###各種操作
list_animal.insert(index,name)
list_animal.pop(-1)
list_animal.sort()

###出力
print(list_animal, end = "")