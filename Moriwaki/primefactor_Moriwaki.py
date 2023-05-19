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

###素数で割る
s = True
t = True
while s:
    for k in list_prime:
        
        while t:
            if num % k == 0:
                list_ans.append(k)
                num = num // k
                t = False
            s = False


print(list_ans,list_prime,num)

