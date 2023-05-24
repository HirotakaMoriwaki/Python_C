import func_salary as fs
import sys

list_salary = sys.argv[1:]

for salary in list_salary:
    payment, tax = fs.calcsalary(salary)
    print("給与:" + str(salary) + "、支給額:" + str(payment) + "、税額:" + str(tax))