import sys
args = sys.argv

input1 = args[1] 
sum = 0

while True :
    sum += int(input1)
    if sum > 100 : 
        print("Over!")
        break
    elif sum == 100 :
        print("Just 100!")
        break

    