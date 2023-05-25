import qrcode
import sys
import os

args = sys.argv
URL = args[1]
name = args[2]
s1 = ".png"
s3 = name + s1
path = os.path.join("../../", "files", s3)
img = qrcode.make("URL")
img.save(path)