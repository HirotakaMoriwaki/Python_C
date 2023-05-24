import sys
from decimal import Decimal, ROUND_HALF_UP

salary = sys.argv[1]
if int(salary) > 1000000 :
    tax = Decimal(100000 + ( int(salary) - 1000000)* 0.2).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    sikyu = int(salary) - tax
    print("支給額:" + str(sikyu) + "、", end="")
    print("税額:" + str(tax), end="")

else :
    tax = Decimal(int(salary)*0.1).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    sikyu = int(salary) - tax
    print("支給額:" + str(sikyu) + "、", end="")
    print("税額:" + str(tax), end="")

