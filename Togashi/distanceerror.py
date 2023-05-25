distance = {'東京': 0.00, '品川':6.78, '新横浜':25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}

import sys
args = sys.argv
eki1 = args[1]
eki2 = args[2]
# キーの値を取得

while True:
    try:
        dis1 = distance[eki1]
        dis2 = distance[eki2]
            # 距離計算
        kyori = dis2-dis1
        # 負の数を正に
        if kyori < 0:
             kyori *= -1.0
        print('{:.2f}'.format(kyori),end="")
        break
    except:
        print("のぞみの停車駅を引数に設定してください")
        break

