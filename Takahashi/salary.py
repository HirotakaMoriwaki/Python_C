from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

salary = args[1]

if int(salary) >1000000:
    tax_rate = (int(salary)-1000000)*0.2
    tax = 100000 + tax_rate
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) 
    pay_amout = int(salary) - tax
    print("支給額:"+str(pay_amout)+"、税額:"+str(tax),end="")

else:
    tax = int(salary) * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) 
    pay_amout = int(salary) - tax
    print("支給額:"+str(pay_amout)+"、税額:"+str(tax),end="")



 