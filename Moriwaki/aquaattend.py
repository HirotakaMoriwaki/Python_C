import sys
import datetime as dt
from datetime import date
from database import session
from tables import Attendnum
from sqlalchemy import func

list_attend = sys.argv[1:]

print(list_attend)

yyyy = int(list_attend[0][:4])
mm = int(list_attend[0][4:6])
dd = int(list_attend[0][6:])
day = dt.date(yyyy,mm,dd)

if session.query(Attendnum).filter(Attendnum.entry_date == day).order_by(Attendnum.seq.desc()).first() == None:
    seq = 1
else:
    seq = session.query(Attendnum).filter(Attendnum.entry_date == day).order_by(Attendnum.seq.desc()).first() + 1

insert = Attendnum(
    entry_date = day,
    seq = seq,
    adult = int(list_attend[1]),
    child = int(list_attend[2])
)


session.add(Attendnum)
session.commit()