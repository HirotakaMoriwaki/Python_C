import sys
args = sys.argv

ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
print(ranking[int(args[1])-1],end="")