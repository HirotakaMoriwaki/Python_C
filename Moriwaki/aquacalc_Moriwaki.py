import sys
import datetime as dt

list_price = [2000, 1200, 2400, 1500] 
list_input = sys.argv[1:]
yyyy = int(list_input[0][:4])
mm = int(list_input[0][4:6])
dd = int(list_input[0][6:])

day = dt.date(yyyy,mm,dd)
date = day.strftime("%w")

if date == "0" or date == "6":
    print(int(list_input[1])*list_price[2] + int(list_input[2])*list_price[3], end = "")
else:
    print(int(list_input[1])*list_price[0] + int(list_input[2])*list_price[1], end = "")