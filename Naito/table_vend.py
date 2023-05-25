import sys
from sqlalchemy import Column,String,Date,Integer
from database import Base
from database import ENGINE

#テーブル
#商品マスタ
class Mst(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id',String(10),primary_key=True)
    name = Column('name',String(20))
    price = Column('price',Integer)

#商品在庫テーブル
class Tbl_stock(Base):
    __tablename__ = 'tbl_stock'
    id = Column('id',String(10),primary_key=True)
    stock = Column('stock',Integer)

#貨幣格納テーブル
class Tbl_money(Base):
    __tablename__ = 'tbl_money'
    price = Column('price',Integer,primary_key=True)
    number = Column('number',Integer)

#メッセージテーブル
class Tbl_message(Base):
    __tablename__ = 'tbl_message'
    seq = Column('seq',Integer,primary_key=True)
    message = Column('message',String(100))
    datetime = Column('datetime',Date)

def main(args):
    #メイン関数
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)

    