#値引き後の価格表示
import sys


args = sys.argv
h = args[1]
d_price = int(args[2])

hinmoku={"リンゴ":80 , "みかん":198, "バナナ":150,
    "ビール":360, "日本酒":580, 
    "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

if(h=='果物類'):
    for i in range(0,3):
        hinmoku[fruits[i]]=hinmoku[fruits[i]]-d_price
        if(hinmoku[fruits[i]] < 1):
            hinmoku[fruits[i]]=1
elif(h=='酒類'):
    for i in range(0,2):
         hinmoku[alcohol[i]]=hinmoku[alcohol[i]]-d_price
         if(hinmoku[alcohol[i]] < 1):
            hinmoku[alcohol[i]]=1
elif(h=='麺類'):
     for i in range(0,3):
         hinmoku[noodles[i]]=hinmoku[noodles[i]]-d_price
         if(hinmoku[noodles[i]] < 1):
            hinmoku[noodles[i]]=1

print(hinmoku,end="")
