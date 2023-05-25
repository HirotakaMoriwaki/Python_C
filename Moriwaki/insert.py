from datetime import date
from database import session
from tables import Tbl_money

prices = (10000, 5000, 2000, 1000, 500, 100, 50, 10)
stocks = (8, 1, 0, 21, 25, 350, 400, 760)

for i in range(len(prices)):
    Tbl = Tbl_money(
        price = prices[i],
        number = stocks[i]
    )
    session.add(Tbl)


session.commit()