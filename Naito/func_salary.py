
from decimal import Decimal, ROUND_HALF_UP 
#支給額と税金を求める関数
def calc_salary(salary):
    #税額を求める
    if(salary > 1000000):
        tax_per = 0.2
        tax = 100000 + ((salary-1000000)*tax_per)
    else:
        tax_per = 0.1
        tax = salary * tax_per
    #四捨五入をする
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    #支給額を求める
    income = salary-tax
    
    return income,tax 