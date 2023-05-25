from  database import session #データベースの接続
from  table_vend import Mst,Tbl_stock,Tbl_money,Tbl_message #テーブル定義
from datetime import date
from sqlalchemy import and_

#商品テーブルから在庫が０以外の商品を取り出す
s_t =  session.query(Mst).filter(and_(Mst.id==Tbl_stock.id,Tbl_stock.stock > 0)).all()
print(s_t)
print(type(s_t))
