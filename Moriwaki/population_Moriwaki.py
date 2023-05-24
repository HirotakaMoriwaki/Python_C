import sys
###入力を受け取りrankに格納
rank = int(sys.argv[1])


list_rank = ("China", "India", "U.S.A", "Indonesia", 
        "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

###該当順位の国名を出力
print(list_rank[rank - 1], end = "")