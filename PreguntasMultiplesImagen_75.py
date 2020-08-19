from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen75_d   import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from comporEdit_TextEdit import comporEdit_TextEdit
from comporSelecBtnsResp import comporSelecBtnsResp

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiplesImagen75(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosPreg = (self.btn_pregIzq, self.btn_pregCen, self.btn_pregDer)
        self.control = comporEdit_TextEdit(self.listBtnPosPreg, self.dSpin_pregTam, [self.txtEdit_preg])

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosResp = (self.btn_respIzq, self.btn_respCen, self.btn_respDer)
        self.control2 = comporEdit_TextEdit(self.listBtnPosResp, self.dSpin_respTam,
                                            [self.txtEdit_respA, self.txtEdit_respB, self.txtEdit_respC,
                                             self.txtEdit_respD])


        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnPunterosResp = (self.btn_respA, self.btn_respB, self.btn_respC, self.btn_respD)
        self.control3 = comporSelecBtnsResp(self.listBtnPunterosResp)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiplesImagen75()
    application.show()
    app.exec()
    #sys.exit(app.exec())
