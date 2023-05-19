#給与を求めるコード
import sys
from decimal import Decimal, ROUND_HALF_UP 

args = sys.argv

#変数に代入
salary = int(args[1])

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
print("支給額:"+str(income)+"、税額:"+str(tax),end="")