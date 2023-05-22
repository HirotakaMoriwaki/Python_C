import sys
num = int(sys.argv[1])
list_ans = []
list_prime = []

###素数判別アルゴリズム
def check(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

###素数の列挙
for j in range(2,num):
    if check(j) == True:
        list_prime.append(j)

###素数で割るアルゴリズム
def devide_prime(n,list1, list2):
    for i in list1:
        if n % i == 0:
            list2.append(i)
            return devide_prime(n//i,list1,list2)
    list2.append(n)

###実際に計算する

devide_prime(num,list_prime,list_ans)
if list_ans.count(1) != 0:
    list_ans.remove(1)

print(list_ans, end = "")