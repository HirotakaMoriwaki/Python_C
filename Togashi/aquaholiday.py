import sys
from datetime import date

from database import session
from tables import Holiday

args = sys.argv
day = args[1]

num_adult = int(args[2])
num_child = int(args[3])
sum = 0
dt = date(int(day[0:4]),int(day[4:6]),int(day[6:8]))

#holidaylist = session.query(Holiday.holi_date, Holiday.holi_text).all()

# 取り出し例
#for ho in holidaylist:
#    print(ho)

user_cnt = int(session.query(Holiday).filter_by(holi_date=dt).count())

if dt.strftime("%a") == "Sun" or dt.strftime("%a") == "Sat":
    sum += 2400 * num_adult
    sum += 1500 * num_child
elif user_cnt == 1:
    sum += 2400 * num_adult
    sum += 1500 * num_child
else:
    sum += 2000 * num_adult
    sum += 1200 * num_child

print(str(sum), end="")