###品目リストの作成
dict_menu = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130,}

###品目表示の関数作成
def dispMenu(dict: dict):
    for i in dict:
        print(i + "：" + str(dict[i]))
        print("投入金額を入力してください")


###投入金額の判定アルゴリズム
def checkMoney(money: int,dict: dict):
    money = int(input("投入金額を入力してください"))

    if money < min(dict.values):
        print(str(money) + "円では購入できる商品がありません。再度投入金額を入力してください")
        return checkMoney(money: int,dict: dict)
    
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        return checkMoney(money: int,dict: dict)
    
    if money % 10 != 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        return checkMoney(money: int,dict: dict)
    
    return buy(money,dict)

###購入アルゴリズム
def buy(money: int,dict: dict):
    menu = input("何を購入しますか（商品名/cancel）")
    if menu == "cancel":
        return charge(money)
    else:
        menu_price = dict[menu]
        leaveMoney = money - menu_price
        if leaveMoney >= min(dict.values):
            print("残金：" + str(leaveMoney) + "円")
            return buy_other(leaveMoney,dict)
        else:
            return charge(leaveMoney)

###続けて購入する場合のアルゴリズム
def buy_other(money: int,dict: dict):
    flag = input("続けて購入しますか（Y/N）")
    if flag == "N":
        return charge(money)
    else:
        for i in dict:
            print(i + "：" + str(dict[i]))
        return buy(money,dict)


###おつり格納リスト
list_charge = [0,0,0,0,0,0,0,0]
list_subject = [10000,5000,2000,1000,500,100,50,10]


###おつり計算アルゴリズム
def charge(money: int, list_charge: list):
    if money // 10000 >= 1:
        list_charge[0] += 1
        return charge(money - 10000)
    elif money // 5000 >= 1:
        list_charge[1] += 1
        return charge(money - 5000)
    elif money // 2000 >= 1:
        list_charge[2] += 1
        return charge(money - 2000)
    elif money // 1000 >= 1:
        list_charge[3] += 1
        return charge(money - 1000)
    elif money // 500 >= 1:
        list_charge[4] += 1
        return charge(money - 500)
    elif money // 100 >= 1:
        list_charge[5] += 1
        return charge(money - 100)
    elif money // 50 >= 1:
        list_charge[6] += 1
        return charge(money - 50)
    elif money // 10 >= 1:
        list_charge[7] += 1
        return charge(money - 10)


###おつり出力アルゴリズム
