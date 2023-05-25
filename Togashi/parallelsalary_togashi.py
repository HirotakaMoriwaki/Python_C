import sys
import func_salary_togashi

args = sys.argv
num = len(args)

for i in range(1, num) :
    salary = int(args[i])
    argsalary = func_salary_togashi.calcsalary(salary)
    payment = argsalary[0]
    tax = argsalary[1]
    print("給与"+ str(salary)+"、支給額:" + str(payment)+"、税額:"+str(tax))