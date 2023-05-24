from datetime import date
import sys
import math
from database import session
from attendnum import attendnum
from sqlalchemy import func

args = sys.argv

input1 = int(args[1])
input2 = int(args[2])
input3 = int(args[3])

Y = input1 % 10000
M = Y % 100


dt = date(math.floor(input1 / 10000), math.floor((input1 % 10000) / 100),math.floor(M % 100))

name_count = session.query(attendnum).filter_by(entry_date = dt).count() + 1
print(name_count)


attend = attendnum(
    entry_date = dt,
    seq = name_count,
    adult = input2,
    child = input3
)
session.add(attend)

session.commit()