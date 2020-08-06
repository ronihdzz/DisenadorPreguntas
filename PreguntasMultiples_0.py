from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen0_d  import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial
#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS



#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiples(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        #Alinear pregunta...

        self.COLOR_NORMAL="#EEF2F3"
        self.COLOR_SELECCION= "#9AE5E0"
        #self.COLOR_RESPUESTA="#9AE5E0"
        #self.COLOR_SELECTION="#CB77D1"

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"
        # self.COLOR_RESPUESTA="#9AE5E0"
        # self.COLOR_SELECTION="#CB77D1"


        self.listImagBtnPos=    ["ICONOS/alinear_centrar.png",
                                 "ICONOS/alinear_izquierda.png",
                                 "ICONOS/alinear_derecho.png"
                                 ]

        self.posPregunta = -1  # 0=centrado 1=izquierda 2=derecha
        self.listBtnPosPreg=[self.btn_pregCen,self.btn_pregIzq,self.btn_pregDer]

        self.posRespuesta=-1  #0=centrado 1=izquierda 2=derecha
        self.listBtnPosResp=[self.btn_respCen,self.btn_respIzq,self.btn_respDer]

        self.editPosPregunta(0)
        self.editPosRespuesta(0)


        for x in range(len(self.listBtnPosPreg)):
            self.listBtnPosPreg[x].clicked.connect(partial(self.editPosPregunta,x))

        for x in range(len(self.listBtnPosResp)):
            self.listBtnPosResp[x].clicked.connect(partial(self.editPosRespuesta, x))

    def editPosPregunta(self, newPosicion):
        print(newPosicion)
        if newPosicion != self.posPregunta:
            self.listBtnPosPreg[self.posPregunta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                    f"border-image: url({self.listImagBtnPos[self.posPregunta]});")
            self.posPregunta=newPosicion
            self.listBtnPosPreg[self.posPregunta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                    f"border-image: url({self.listImagBtnPos[self.posPregunta]});")

    def editPosRespuesta(self, newPosicion):
        print(newPosicion)
        if newPosicion != self.posRespuesta:
            self.listBtnPosResp[self.posRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                    f"border-image: url({self.listImagBtnPos[self.posRespuesta]});")
            self.posRespuesta=newPosicion
            self.listBtnPosResp[self.posRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                    f"border-image: url({self.listImagBtnPos[self.posRespuesta]});")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiples()
    application.show()
    app.exec()
    #sys.exit(app.exec())


#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke

# self.btn_pregCen.clicked.connect(lambda: self.editPosPregunta(0))
# self.btn_pregIzq.clicked.connect(lambda: self.editPosPregunta(1))
# self.btn_pregDer.clicked.connect(lambda: self.editPosPregunta(2))