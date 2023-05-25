import sys
from datetime import date

from database import session
from tables import Attendnum

args = sys.argv
day = args[1]

num_adult = int(args[2])
num_child = int(args[3])
dt = date(int(day[0:4]),int(day[4:6]),int(day[6:8]))

user_cnt = int(session.query(Attendnum).filter_by(entry_date=dt).count())+1

attendnum = Attendnum(
    entry_date=dt,
    seq = user_cnt,
    adult = num_adult,
    child = num_child
)



session.add(attendnum)

session.commit()