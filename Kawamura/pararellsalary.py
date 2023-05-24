import func_salary
import sys

salary = sys.argv[1]

tax,sal = func_salary.calcsalary(salary)
print("給与:"+str(salary)+"、"+"支給額:"+str(sal)+"、"+"税額:"+str(tax), end="")


