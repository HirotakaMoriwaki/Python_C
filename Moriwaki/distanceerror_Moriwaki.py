import sys
distance = {"東京":0.00,
            "品川":6.78,
            "新横浜":25.54,
            "名古屋":342.02,
            "京都":476.31,
            "新大阪":515.35
            }
while True:
    try:

###スタートとゴールの”東京からの距離”を格納
        start = distance[sys.argv[1]]
        goal = distance[sys.argv[2]]

###スタートとゴールの距離の絶対値を求める
###小数点以下2位に丸めこむ
        print('{:.2f}'.format(abs(goal - start)) , end = "")
        break;

    except:
        print("のぞみの停車駅を引数に設定してください", end = "")
        break;