from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QTextEdit,QCheckBox,QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespCheckBoxImagen0_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial

from comporEdit_TextEdit import comporEdit_TextEdit
from comporSelecBtnsResp import comporSelecBtnsResp
#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from functools import partial
import numpy as np
from PyQt5.QtWidgets import  QMessageBox



#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaCheckBoxImagen_0(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.NO_RESPUESTAS_IMAGEN = 0



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaCheckBoxImagen_0()
    application.show()
    app.exec()
    #sys.exit(app.exec())



#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke

'''
        for i in reversed(range(layout.count())):
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)


https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt



'''

'''
   widget.setStyleSheet("margin: 1px;")
widget.setMinimumHeight(70)
widget.setMaximumHeight(70)
hBoxLoyout = QHBoxLayout(widget)  # Set the checkbox in the layer

checkBox=QCheckBox()
checkBox.setStyleSheet("QCheckBox::indicator {width:30px; height:30px; }"
                       "QCheckBox::indicator:pressed{background-color:#0C868C;}"
                      )
textEdit=QTextEdit()
hBoxLoyout.addWidget(checkBox)
hBoxLoyout.addWidget(textEdit)

widgetTotal=QWidget()
vBoxLayout=QVBoxLayout(widgetTotal)
botonCerrar=QPushButton()
botonCerrar.setMaximumSize(15,15)
botonCerrar.setMinimumSize(15,15)
vBoxLayout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding
hBoxLoyout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding
vBoxLayout.addWidget(botonCerrar,alignment=QtCore.Qt.AlignRight)
vBoxLayout.addWidget(widget)

self.vbox.addWidget(widgetTotal)
else:
QMessageBox.question(self, "DelphiPreguntas",
                      "El numero maximo de items es de:\n"
                     f"{self.MAX_ITEMS} items, y usted ya ha llegado\n"
                      "a dicho limite.",
                     QMessageBox.Ok)         


'''
