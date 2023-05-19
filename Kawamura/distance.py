import sys
args = sys.argv

input1 = args[1] 
input2 = args[2]

distance = {
    '東京':0.00,
    '品川':6.78,
    '新横浜':25.54,
    '名古屋':342.02,
    '京都':476.31,
    '新大阪':515.35,
}

distance_between = distance[input2] - distance[input1] # 距離を求める

print(abs(round(distance_between,2)), end="") # 四捨五入小数点第二位までかつ絶対値を指定