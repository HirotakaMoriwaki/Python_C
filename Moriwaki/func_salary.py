from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    salary = int(salary)
    if salary > 1000000:
        tax = ( salary - 1000000 )*0.2 + 100000
    else:
        tax = salary * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    payment = salary - tax
    return payment, tax