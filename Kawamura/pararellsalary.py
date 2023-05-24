import func_salary
import sys

salary1 = sys.argv[1]
salary2 = sys.argv[2]
salary3 = sys.argv[3]

tax,sal = func_salary.calcsalary(salary1)
print("給与:"+str(salary1)+"、"+"支給額:"+str(sal)+"、"+"税額:"+str(tax))
tax,sal = func_salary.calcsalary(salary2)
print("給与:"+str(salary2)+"、"+"支給額:"+str(sal)+"、"+"税額:"+str(tax))
tax,sal = func_salary.calcsalary(salary3)
print("給与:"+str(salary3)+"、"+"支給額:"+str(sal)+"、"+"税額:"+str(tax))

