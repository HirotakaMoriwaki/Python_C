import sys
args = sys.argv
# 素因数を入れるリストprimefactor
primefactor = []
# エラー処理

# 引数が正しく設定されたとき
try:
    # 引数を変数に設定
    num = int(args[1])
    while True:
        # numが2未満ならループ脱出
        if 2 > num:
            break
        # 2以上であれば素因数分解
        # 2から数を増やして割っていく
        for i in range(2, num+1):
            # numがiで割り切れる場合
            if num % i == 0:
                # numをiで割った数をnew_numに設定
                new_num = int(num / i) 
                # i=素因数をリストに追加
                primefactor.append(i)
                # 数字を更新
                num = new_num
                # ループに戻る
                break
    # 素因数分解が終了
    # リストの印刷
    print(primefactor)
    
# 引数が正しく設定されなかったとき
except:
    print("正しい引数を設定してください")
        