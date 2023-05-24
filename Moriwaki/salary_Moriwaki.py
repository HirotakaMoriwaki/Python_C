from decimal import Decimal, ROUND_HALF_UP
import sys

#給与の入力を受け取る。税率を入れるtaxを用意。
salary_ex = int(sys.argv[1])
tax = 0

#給与の額に応じて条件分岐
if salary_ex >= 1000000:
    tax += (salary_ex - 1000000) * 0.2 + 100000
else:
    tax += salary_ex * 0.1

#税額を四捨五入
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

#支給額と税額を出力
print("支給額:" + str(salary_ex-tax) + "、税額:" + str(tax) , end="")