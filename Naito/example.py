from  database import session
from  tables import Holiday

holidaylist = session.query(Holiday).all()
