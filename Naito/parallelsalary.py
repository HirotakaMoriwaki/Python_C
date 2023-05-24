import func_salary
import sys

args = sys.argv
s = [] #給与を格納する配列

#引数の格納
for i in range(1,len(args)):
    s.append(int(args[i]))

#支給額と税額の表示
for j in range(len(s)):
    income,tax=func_salary.calc_salary(s[j])
    print(' 給与:{0}、支給額:{1}、税額:{2}'.format(s[j],income,tax))