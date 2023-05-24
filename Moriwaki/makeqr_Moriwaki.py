import qrcode
import sys
import os

URL = sys.argv[1]
PATH = os.path.join("..","files",sys.argv[2])

img = qrcode.make(URL)
img.save(PATH)