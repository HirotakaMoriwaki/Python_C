from datetime import date
import sys
import math
from database import session
from tables import Holiday
from sqlalchemy import func
args = sys.argv

input1 = int(args[1])
input2 = int(args[2])
input3 = int(args[3])

# 20220603
Y = input1 % 10000
M = Y % 100


dt = date(math.floor(input1 / 10000), math.floor((input1 % 10000) / 100),math.floor(M % 100))
youbi = dt.strftime("%a")

name_count = session.query(func.count(Holiday.holi_date)).filter_by(holi_date = dt).first()
print(name_count)
print(name_count)
if youbi == "Sat" or youbi == "Sun" or name_count[0] == 1:
    sum = input2 * 2400 +  input3 * 1500
    print(sum,end="") 

if (youbi == "Mon" or youbi == "Tue" or youbi == "Wed" or youbi == "Thu" or youbi == "Fri") and name_count[0] != 1:
    sum = input2 * 2000 +  input3 * 1200
    print(sum,end="") 