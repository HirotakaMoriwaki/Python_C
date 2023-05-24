import sys
import introduce

args = sys.argv

#引数を変数に代入
input1 = args[1]
input2 = args[2]

# インスタンスを生成
intro = introduce.Intro(input1, input2)
print(intro.name_out())
print(intro.age_out())


