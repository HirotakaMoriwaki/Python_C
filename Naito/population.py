#引数番目の国を表示するプログラム
import sys

args=sys.argv
rank=int(args[1])
#国のランキングのタプル
con = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
print(con[rank-1],end="")