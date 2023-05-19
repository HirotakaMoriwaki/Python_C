#引数受け取り
import sys
args = sys.argv
math = int(args[1])
jap = int(args[2])
eng = int(args[3])

# 全科目が70点以上
if math>=70 and jap>= 70 and eng >= 70:
    print("合格", end="")
elif math+jap+eng >= 220:
    if math >=50 and jap >= 50 and eng >= 50:
        # 合計点が220点以上かつ50点未満がない
        print("合格", end="")
    else:
        # 合計点が220点以上だが50点未満がある
        print("不合格", end="")
else: 
    # 70点以上ではない科目があり、合計点も220点未満
    print("不合格", end="")
