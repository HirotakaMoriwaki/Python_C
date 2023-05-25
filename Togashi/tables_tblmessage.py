import sys
from sqlalchemy import Column, Integer, DateTime, String
from database import Base
from database import ENGINE

class tbl_message(Base):
    __tablename__='tbl_message'
    seq = Column('seq', Integer, primary_key = True)
    message = Column('message', String(20))
    datetime = Column('datetime', DateTime)

def main (args):
    """メイン関数"""
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)