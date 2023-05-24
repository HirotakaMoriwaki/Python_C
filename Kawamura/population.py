import sys
args = sys.argv

input1 = int(args[1])

rank = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(rank[input1-1], end="")