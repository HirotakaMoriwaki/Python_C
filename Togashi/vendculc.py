# 辞書作成
products = {'お茶': 110, 'コーヒー':100, 'ソーダ':160, 'コーンポタージュ':130}
# 辞書名のリスト
products_name = list( products.keys())
# おつりの計算関数
def calc_change(money):
    num_5000 = 0
    num_2000 = 0
    num_1000 = 0
    num_500 = 0
    num_100 = 0
    num_50 = 0
    num_10 = 0
    while money != 0:
        if money >= 5000:
            money = money - 5000
            num_5000 += 1
        elif money >= 2000:
            money = money - 2000
            num_2000 += 1
        elif money >= 1000:
            money = money - 1000
            num_1000 += 1
        elif money >= 500:
            money = money - 500
            num_500 += 1
        elif money >= 100:
            money = money - 100
            num_100 += 1
        elif money >= 50:
            money = money - 50
            num_50 += 1
        elif money >= 10:
            money = money - 10
            num_10 += 1
    if num_5000 > 0:
        print("5000円札："+str(num_5000)+"枚")
    if num_2000 > 0:
        print("2000円札："+str(num_2000)+"枚")
    if num_1000 > 0:
        print("1000円札："+str(num_1000)+"枚")
    if num_500 > 0:
        print("500円玉："+str(num_500)+"枚")
    if num_100 > 0:
        print("100円玉："+str(num_100)+"枚")
    if num_50 > 0:
        print("50円玉："+str(num_50)+"枚")
    if num_10 > 0:
        print("10円玉："+str(num_10)+"枚")

def name_check(name):
    num = products_name.count(name)
    return num


# 辞書の中身書き出し
for product in products:
    print(product,end="")
    print("：",end="")
    print(products[product],end="")
    print("円")

while True:
    money = int(input("投入金額を入力してください"))
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度導入金額を入力してください")
    elif money < 100:
        print(str(money)+"円では購入できる商品がありません。再度導入金額を入力してください")
    elif money % 10 != 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
    else:
        name = input("何を購入しますか？（商品名/cancel）")
        pro_exist = name_check(name)
        print(str(pro_exist))
        if name == "cancel":
            calc_change(money)
        elif pro_exist == 0:
            break
        else:
            while True:
                money = money - products[name]
                if money >= 100:
                    print("残金：",end="")
                    print(str(money), end="") 
                    print("円")
                    next = input("続けて購入しますか（Y/N）")
                    if next == "Y":
                        for product in products:
                            print(product,end="")
                            print("：",end="")
                            print(products[product],end="")
                            print("円")
                        name = input("何を購入しますか？（商品名/cancel）")
                        pro_exist = name_check(name)
                        while pro_exist == 0:
                            name = input("何を購入しますか？（商品名/cancel）")
                            pro_exist = name_check(name)
                    
                    else:
                        print("おつり")
                        calc_change(money)
                        break
                else:
                    print("おつり")
                    calc_change(money)
                    break
        break
            

