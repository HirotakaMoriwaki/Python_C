#素因数分解の結果を求める
import sys

#引数を代入
args = sys.argv
k=int(args[1])

#素因数分解の結果を格納するリスト
l=[]

#素因数判定
for i in range(2,k+1):
    while True:
        # 余り0ならストにappend
        if k%i == 0:
            l.append(i)
            k = k/i 
           # print("k={}".format(k)) # nの更新状況をみてみる
        else:
            break
print(l,end="")