import sys

####数値入力を受け取り初期値としてnum_initとnumに反映させる####
num_init = int(sys.argv[1])
num = num_init

####繰り返し操作・numにnum_initを足し続けnumを評価####
while True:
    if num == 100:
        print("Just 100!")
        break
    elif num < 100:
        num += num_init
    else:
        print("Over!")
        break