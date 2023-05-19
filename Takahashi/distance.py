import sys
args = sys.argv

distance = {'東京':0.00, '品川':6.78, '新横浜':25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}
sta1 = args[1]
sta2 = args[2]
if distance[sta1] > distance[sta2]:
    d = (distance[args[2]] - distance[args[1]]) * -1
    print('{:.2f}'.format(d),end="")
else:
    d = distance[args[2]] - distance[args[1]]
    print('{:.2f}'.format(d),end="")

