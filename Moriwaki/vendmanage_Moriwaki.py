import datetime
from database import session
from tables import Mst_merchandise, Tbl_stock, Tbl_money, Tbl_message
from sqlalchemy import func

###メニュー表示関数
def dispMenu():
    menulist = session.query(Mst_merchandise, Mst_merchandise.id, Mst_merchandise.name, Mst_merchandise.price, Tbl_stock.stock).join(Tbl_stock, Mst_merchandise.id == Tbl_stock.id).all()
    current_price = dict()
    current_stock = dict()
    for i in menulist:
        if i.stock > 0:
            print(i.name + "：" + str(i.price) + "円")
            current_price[i.id] = i.price
            current_stock[i.id] = i.stock
    return checkMoney(0, current_price)


###金額チェック関数
def checkMoney(money,dict: dict):
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
    
    return buy(money)


dispMenu()