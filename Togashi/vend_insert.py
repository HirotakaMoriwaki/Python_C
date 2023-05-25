from datetime import date
from database import session
from tables import tbl_money

tbl_money = tbl_money(
    price = 10,
    number = 4
)
session.add(tbl_money)

session.commit()