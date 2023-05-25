from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    if salary <= 1000000:
    # 税率10%
        tax = salary * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        payment = salary - tax
        # 100万円より多い場合
    else:
        # 100万を超えた分は税率20%
        tax = (salary-1000000) * 0.2
        # 四捨五入
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        tax = tax + 100000
        payment = salary - tax
    return (payment, tax)