from datetime import date
import datetime
import sys
from  database import session #データベースの接続
from  table_vend import Mst,Tbl_stock#テーブル定義

menu = {
    'お茶':110,
    'コーヒー':160,
    'ソーダ':160,
    'コーンポタージュ':130
}
i_d = ['A000000001','B000000001','C000000001','D000000001']
i=0

#商品テーブルに値を格納する
#key1にお茶などの名前格納　idは１から
# for key1 in menu.keys():
#     #追加するデータ
#     mst = Mst(
#         id = i_d[i],
#         name =  key1,
#         price = menu[key1],
#     )
#     i+=1
#     #INSERT
#     session.add(mst)
#     #コミット
#     session.commit()


#商品在庫テーブルに値を格納する
#在庫
i=0
s_t = [0,20,20,100]
for key1 in menu.keys():
    tbl_s = Tbl_stock(
        id = i_d[i],
        stock = s_t[i]
    )
    i+=1
    #INSERT
    session.add(tbl_s)
    #コミット
    session.commit()

