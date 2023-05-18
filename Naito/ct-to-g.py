#カラットをグラムに変換する
#変換の元になる
per_ct=0.2
#ユーザからの入力
user = input('何カラットですか')
ct= float(user)
#計算
g = ct*per_ct
#結果の表示
desc = '{0}カラット-{1}グラム'.format(ct,g)
print(desc)