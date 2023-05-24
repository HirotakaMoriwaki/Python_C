#モジュール「os」のimport
import os
import qrcode
#os.path.joinを利用して相対パスを生成する
#相対パス（"../files/xxxxxx.png"）となる
path = os.path.join("..",  "files",  "qr.png")
#png ファイルの生成
img = qrcode.make("https://www.bing.com/ck/a?!&&p=afc363a28be0fd1eJmltdHM9MTY4NDgwMDAwMCZpZ3VpZD0zNjA2Mzc0NC0zNjAzLTZlOTItMzNlMy0yNWIxMzdmMTZmNDcmaW5zaWQ9NTE5Ng&ptn=3&hsh=3&fclid=36063744-3603-6e92-33e3-25b137f16f47&psq=the+oral+cigarettes&u=a1aHR0cHM6Ly90aGVvcmFsY2lnYXJldHRlcy5jb20v&ntb=1")
img.save(path)

