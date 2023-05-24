from datetime import date
import sys
import math
from database import session
from tables import Holiday
args = sys.argv


holidaylist = session.query(Holiday.holi_date).all()

print(holidaylist[1])