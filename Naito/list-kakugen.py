import random 

#格言をリストに代入
kakugen = [
    "能ある鷹は爪を隠す",
    "豚に真珠",
    "二兎を追うものは一兎をも得ず",
    "叩き続けなさい。そうすれば開かれます。"
]
print(kakugen)
#ランダムに数値を一つ選ぶ
i = random.randint(0,len(kakugen)-1)
print(i)
#選んだ格言を表示する
print( kakugen[i] )