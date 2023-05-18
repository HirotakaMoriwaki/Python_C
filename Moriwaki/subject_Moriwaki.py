import sys

#点数の入力を受け取る。リストの全要素をint型にする。
list_score = sys.argv[1:4]
for i in range(3):
    list_score[i] = int(list_score[i])

#点数に応じて条件分岐
if (sum(list_score) >= 220) or (list_score[0]>=70 and list_score[1]>=70 and list_score[2]>=70):
    if (list_score[0]>=50 and list_score[1]>=50 and list_score[2]>=50):
        print("合格",end="")
    else:
        print("不合格",end="")
else:
    print("不合格",end="")