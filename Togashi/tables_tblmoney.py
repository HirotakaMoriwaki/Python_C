import sys
from sqlalchemy import Column, Integer, DateTime, String
from database import Base
from database import ENGINE

class tbl_money(Base):
    __tablename__='tbl_money'
    price = Column('price', Integer, primary_key = True)
    number = Column('number', Integer)

def main (args):
    """メイン関数"""
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)