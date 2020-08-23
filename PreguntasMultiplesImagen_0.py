from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen0_d  import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial

from comporEdit_TextEdit import comporEdit_TextEdit
from comporSelecBtnsResp import comporSelecBtnsResp
#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from functools import partial
import numpy as np


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiplesImagen_0(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiplesImagen_0()
    application.show()
    app.exec()
    #sys.exit(app.exec())


'''

## Comportamiento de las ediciones de un edit text...
        self.listBtnPosPreg=(self.btn_pregIzq,self.btn_pregCen,self.btn_pregDer)
        self.control=comporEdit_TextEdit(self.listBtnPosPreg,self.dSpin_pregTam,[self.txtEdit_preg])

        self.txtEdit_preg.textChanged.connect(self.imprimir)

## Comportamiento de las ediciones de un edit text...
        self.listBtnPosResp=(self.btn_respIzq,self.btn_respCen,self.btn_respDer)
        self.control2 = comporEdit_TextEdit(self.listBtnPosResp, self.dSpin_respTam,[self.txtEdit_respA,self.txtEdit_respB,self.txtEdit_respC,self.txtEdit_respD])


#Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnPunterosResp=(self.btn_respA,self.btn_respB,self.btn_respC,self.btn_respD)
        self.control3=comporSelecBtnsResp(self.listBtnPunterosResp)


#Lista de respuestas....

        #Texto pregunta....
        self.dataPregunta={"PREGUNTA":[None,None],
                           "RESP_A":[None,None],
                           "RESP_B":[None,None],
                           "RESP_C":[None,None],
                           "RESP_D":[None,None]
                           }

        self.guardarEnListCada=10 #guardar en lista cada 5 caracteres...
        self.puntero_guardarEnListCada=self.guardarEnListCada-5
        self.txtEdit_preg.selectionChanged.connect(self.holi)  #me dira cuando lo seleccionaron...


    def  holi(self):
        print("holi")

    def imprimir(self):
        if self.puntero_guardarEnListCada>self.guardarEnListCada:
            self.puntero_guardarEnListCada=0
            #print(self.txtEdit_preg.toPlainText())
            self.dataPregunta["PREGUNTA"][0]=self.txtEdit_preg.toPlainText()
            print(self.dataPregunta["PREGUNTA"][0])
        self.puntero_guardarEnListCada+=1
'''

#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke

# self.btn_pregCen.clicked.connect(lambda: self.editPosPregunta(0))
# self.btn_pregIzq.clicked.connect(lambda: self.editPosPregunta(1))
# self.btn_pregDer.clicked.connect(lambda: self.editPosPregunta(2))