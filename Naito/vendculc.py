#自販機のお釣りを求める
#お釣りを求めるメゾット
def change(cost):
    money_type = [5000,2000,1000,500,100,50,10]
    print("おつり")
    for money in money_type:
        coin = cost // money # //は切り捨ての割り算
        print(str(money), '円玉' , str(coin) , '枚')
        cost -= coin * money

#メニュー：辞書型
menu = {
    'お茶':110,
    'コーヒー':160,
    'ソーダ':160,
    'コーンポタージュ':130
}

#品目
hinmoku = ['お茶','コーヒー','ソーダ','コーンポタージュ']
list_price =[]

#購入リストの表示
for i in range(len(hinmoku)):
    print(hinmoku[i]+" : "+str(menu[hinmoku[i]])+"円")
    list_price.append(menu[hinmoku[i]])

#金額を入力
cost = int(input("投入金額を入力してください\n"))
#最小値段
m=min(list_price)
next="Y"
hantei = True
#買うものの選択
while hantei:
    if(cost > 10000):
        print("10000円を超える金額は投入できません。",end="")
        cost=int(input("再度投入金額を入力してください\n"))
        continue
    elif(cost < m):
        print(str(cost)+"円では購入できる商品がありません。",end="")
        cost=int(input("再度投入金額を入力してください\n"))
        continue
    elif(str(cost)[-1]!="0"):
        print("1円玉、5円玉は使用できません。",end="")
        cost=int(input("再度投入金額を入力してください\n"))
        continue
    elif(cost >= m and next == "Y"):
        buy = input('何を購入しますか（商品名/cancel）')
        if(buy == 'cancel'):
            change(cost)
            break
        else:
            for j in range(len(hinmoku)):
                if(buy == hinmoku[j]):
                    cost -= menu[hinmoku[j]]
                    print("残金："+str(cost))
                    if(cost==0):
                        hantei = False
                    else:
                        next=input("続けて購入しますか（Y/N）")
                    if(cost < m or next=="N"):
                        change(cost)
                        hantei = False