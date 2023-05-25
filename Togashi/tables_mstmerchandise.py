import sys
from sqlalchemy import Column, Integer, DateTime, String
from database import Base
from database import ENGINE

class mst_merchandise(Base):
    __tablename__='mst_merchandise'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))
    price = Column('price', Integer)

def main (args):
    """メイン関数"""
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)