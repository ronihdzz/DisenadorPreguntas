import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
#https://www.onlinegdb.com/online_python_compiler
#https://repl.it/languages/python3


#EJECUTADOR DE CODIGO...
web = QWebEngineView()
web.load(QUrl("https://www.programiz.com/python-programming/online-compiler/"))
web.show()

sys.exit(app.exec_())