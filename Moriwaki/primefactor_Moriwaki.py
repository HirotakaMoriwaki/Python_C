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
def devide_prime(n,list):
    for i in list:
        if n % i == 0:
            return devide_prime(n//i,list)

###実際に計算する
list_ans.append(num)

while devide_prime(num,list_prime) == False:
    list_ans.append(devide_prime(num,list_prime))
    num = num//devide_prime(num,list_prime)

print(list_prime,list_ans.sort())