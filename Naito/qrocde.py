import qrcode
import os
import sys

#引数の代入
args =sys.argv

url = args[1]
file_name = args[2]

#QRコード作成
img = qrcode.make(url)

path = os.path.join(".",  "Files",  file_name+".png")
img.save(path)