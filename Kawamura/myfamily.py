import sys
import introfamily
args = sys.argv

#引数を変数に代入123
input1 = args[1]
input2 = args[2]
input3 = args[3]

intro = introfamily.IntroFam(input1, input2, input3) # __init__に()内の引数を渡す

print(intro.name_out())
print(intro.age_out())
print(intro.cat_name_out())