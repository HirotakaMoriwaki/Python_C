from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    if int(salary) > 1000000 :
        tax = Decimal(100000 + ( int(salary) - 1000000)* 0.2).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        sikyu = int(salary) - tax
        return tax, sikyu

    else :
        tax = Decimal(int(salary)*0.1).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        sikyu = int(salary) - tax
        return tax, sikyu
