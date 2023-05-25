import sys
args = sys.argv

num= int(args[1])
insu = []

while True:
    if 2 > num:
        break
    for i in range(2, num+1):
        if num % i == 0:
            num2 = int(num / i) 
            insu.append(i)
            num = num2
            break

insu.sort()
print(insu)