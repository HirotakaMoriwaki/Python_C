#値引き後の価格表示
import sys

args = sys.argv
h = args[1]
d_price = int(args[2])

hinmoku={"リンゴ":80 , "みかん":198, "バナナ":150,
    "ビール":360, "日本酒":580, 
    "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")          #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

kids = {
    '果物類':fruits,
    '酒類':alcohol,
    '麺類':noodles
}

for i in range(len(kids[h])):
    hinmoku[kids[h][i]]=hinmoku[kids[h][i]]-d_price
    if(hinmoku[kids[h][i]] < 1):
        hinmoku[kids[h][i]]=1

print(hinmoku,end="")
