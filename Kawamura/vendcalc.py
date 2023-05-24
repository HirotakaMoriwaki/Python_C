from decimal import Decimal, ROUND_HALF_DOWN



print("お茶：110円")
print("コーヒー：100円")
print("ソーダ：160円")
print("コーンポタージュ：130円")
items = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

def oturi(remain_money):
    print("おつり")
    if remain_money > 5000:
        remain_money = remain_money - 5000
        print("5000円：1枚")
    if remain_money > 2000:
        print("2000円：" + str(Decimal(remain_money / 2000).quantize(Decimal("0"),rounding=ROUND_HALF_DOWN)) + "枚") 
        remain_money = remain_money % 2000
    if remain_money > 1000:
        print("1000円：" + str(Decimal(remain_money / 1000).quantize(Decimal("0"),rounding=ROUND_HALF_DOWN)) + "枚") 
        remain_money = remain_money % 1000
    if remain_money > 500:
        print("500円：" + str(Decimal(remain_money / 500).quantize(Decimal("0"),rounding=ROUND_HALF_DOWN)) + "枚") 
        remain_money = remain_money % 500
    if remain_money > 100:
        print("100円：" + str(Decimal(remain_money / 100).quantize(Decimal("0"),rounding=ROUND_HALF_DOWN)) + "枚") 
        remain_money = remain_money % 100
    if remain_money > 50:
        print("50円：" + str(Decimal(remain_money / 50).quantize(Decimal("0"),rounding=ROUND_HALF_DOWN)) + "枚") 
        remain_money = remain_money % 50
    if remain_money > 10:
        print("10円：" + str(Decimal(remain_money / 10).quantize(Decimal("0"),rounding=ROUND_HALF_DOWN)) + "枚") 
        remain_money = remain_money % 10

while True:
    money = int(input("投入金額を入力してください"))

    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        continue
    if money < 100:
        print(str(money) + "円では購入できる商品がありません。再度投入金額を入力してください")
        continue
    if money % 5 == 0 and money % 10 != 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
    else: break


while True:
    select = input("何を購入しますか(商品名/cancel)")
    if money - int(items[select]) >= 100:
        money = money - int(items[select])
        print("残金" + str(money) + "円")
        YN = input("続けて購入しますか(Y/N)")
        if YN == "Y":
            keys = [key for key, value in items.items() if value < money]
            print(keys)
            continue
        if YN == "N":
            oturi(money)
    if money == "cancel":
        oturi(money)
        break




