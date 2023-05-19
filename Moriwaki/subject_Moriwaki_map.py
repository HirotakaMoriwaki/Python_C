import sys

#点数の入力を受け取る。リストの全要素をint型にする。
math, japan, english = map(int,sys.argv[1:4])

#点数に応じて条件分岐
if (sum([math,japan,english]) >= 220) or (math>=70 and japan>=70 and english>=70):
    if (math>=50 and japan>=50 and english>=50):
        print("合格",end="")
    else:
        print("不合格",end="")
else:
    print("不合格",end="")