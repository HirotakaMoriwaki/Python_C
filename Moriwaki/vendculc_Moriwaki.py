###品目リストの作成
dict_menu = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130,}

###品目表示の関数作成
def dispMenu(dict: dict):
    for i in dict:
        print(i + "：" + str(dict[i]))
    return checkMoney(0, dict)


###投入金額の判定アルゴリズム
def checkMoney(money: int,dict: dict):
    money = int(input("投入金額を入力してください"))

    if money < min(dict.values()):
        print(str(money) + "円では購入できる商品がありません。再度投入金額を入力してください")
        return checkMoney(money,dict)
    
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        return checkMoney(money,dict)
    
    if money % 10 != 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        return checkMoney(money,dict)
    
    return buy(money,dict)

###購入アルゴリズム
def buy(money: int,dict: dict):
    menu = input("何を購入しますか（商品名/cancel）")
    if menu == "cancel":
        return charge(money)
    else:
        menu_price = dict[menu]
        leaveMoney = money - menu_price
        if leaveMoney >= min(dict.values()):
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
def charge(money: int):
    for i in range(8):
        if money // list_subject[i] >= 1:
            list_charge[i] += money // list_subject[i]
            money -= (list_subject[i] * list_charge[i])
    return pay_charge()

###おつり出力アルゴリズム
def pay_charge():
    for i in range(8):
        if (list_charge[i] != 0) and (i < 4):
            print(str(list_subject[i]) + "円札：" + str(list_charge[i]) + "枚")
        elif (list_charge[i] != 0) and (i >= 4):
            print(str(list_subject[i]) + "円玉：" + str(list_charge[i]) + "枚")
        




dispMenu(dict_menu)