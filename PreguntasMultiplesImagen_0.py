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
class PreguntasMultiplesImagen_0(QtWidgets.QWidget, Ui_Form):
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


        #Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnPunterosResp=(self.btn_respA,self.btn_respB,self.btn_respC,self.btn_respD)
        self.listRespCorrectas=[False,False,False,False] #todas inicialmente son consideradas
                                                         #incorrectas...
        for x in range(len(self.listBtnPunterosResp)):
            self.listBtnPunterosResp[x].clicked.connect(partial(self.marcarDesmarcarRespuesta,x))




        #Metodologia empleada para el diseño de la  P R E G U N T A y R E S P U E S T A S:
        self.listImagBtnPos=    ["ICONOS/alinear_izquierda.png",
                                 "ICONOS/alinear_centrar.png",
                                 "ICONOS/alinear_derecho.png"
                                 ]
        #Posicion del texto de  la pregunta...
        self.posPregunta = 1  # 0=izquierda 1=centro 2=derecha
        self.listBtnPosPreg=(self.btn_pregIzq,self.btn_pregCen,self.btn_pregDer)
        for x in range(len(self.listBtnPosPreg)):
            self.listBtnPosPreg[x].clicked.connect(partial(self.editPosPregunta,x))
        self.editPosPregunta(1)

        #Posicion del texto de la respuesta
        self.posRespuesta= 1  #0=izquierda 1=centro 2=derecha
        self.listBtnPosResp=(self.btn_respIzq,self.btn_respCen,self.btn_respDer)
        for x in range(len(self.listBtnPosResp)):
            self.listBtnPosResp[x].clicked.connect(partial(self.editPosRespuesta, x))
        self.editPosRespuesta(1)

        #Cambiar tamaño de pregunta....
        self.dSpin_pregTam.setMinimum(8)
        self.dSpin_pregTam.setMaximum(40)
        self.dSpin_pregTam.setValue(15)
        self.cambiarTamPreg(15)
        self.dSpin_pregTam.valueChanged.connect(self.cambiarTamPreg)
        #Cambiar tamaño de las respuestas de la pregunta...
        self.dSpin_respTam.setMinimum(8)
        self.dSpin_respTam.setMaximum(40)
        self.dSpin_respTam.setValue(15)
        self.cambiarTamResp(15)
        self.dSpin_respTam.valueChanged.connect(self.cambiarTamResp)

###################################################################################################
#   S E C C I O N     BOTONES SELECCIONADOS
####################################################################################################
    def marcarDesmarcarRespuesta(self,idBtnRespuesta):
        print("boton:",idBtnRespuesta)
        if self.listRespCorrectas[idBtnRespuesta]==True:
            self.listRespCorrectas[idBtnRespuesta]=False
            self.listBtnPunterosResp[idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                   "border-radius: 20px;"
                                                                   "border: 1px solid #555;")
        else:
            self.listRespCorrectas[idBtnRespuesta]=True
            self.listBtnPunterosResp[idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                   f"border-radius: 20px;"
                                                                   "border: 1px solid #555;")


###################################################################################################
#   S E C C I O N     DISENO DE PREGUNTAS Y RESPUESTAS
####################################################################################################

    def cambiarTamPreg(self,newValor):
        #Cambiando el tamaño
        font = QtGui.QFont()
        font.setPointSize(int(newValor))
        self.txtEdit_preg.setFont(font)

    def cambiarTamResp(self,newValor):
        # Cambiando el tamaño
        font = QtGui.QFont()
        font.setPointSize(int(newValor))
        self.txtEdit_respA.setFont(font)
        self.txtEdit_respB.setFont(font)
        self.txtEdit_respC.setFont(font)
        self.txtEdit_respD.setFont(font)


    def editPosPregunta(self, newPosicion):
            if newPosicion==0:
                self.txtEdit_preg.setAlignment(Qt.AlignLeft)
            elif newPosicion==1:
                self.txtEdit_preg.setAlignment(Qt.AlignHCenter)
            elif newPosicion==2:
                self.txtEdit_preg.setAlignment(Qt.AlignRight)
            self.listBtnPosPreg[self.posPregunta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                    f"border-image: url({self.listImagBtnPos[self.posPregunta]});")
            self.posPregunta=newPosicion
            self.listBtnPosPreg[self.posPregunta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                    f"border-image: url({self.listImagBtnPos[self.posPregunta]});")

    def editPosRespuesta(self, newPosicion):
            if newPosicion==0:
                self.txtEdit_respA.setAlignment(Qt.AlignLeft)
                self.txtEdit_respB.setAlignment(Qt.AlignLeft)
                self.txtEdit_respC.setAlignment(Qt.AlignLeft)
                self.txtEdit_respD.setAlignment(Qt.AlignLeft)
            elif newPosicion==1:
                self.txtEdit_respA.setAlignment(Qt.AlignHCenter)
                self.txtEdit_respB.setAlignment(Qt.AlignHCenter)
                self.txtEdit_respC.setAlignment(Qt.AlignHCenter)
                self.txtEdit_respD.setAlignment(Qt.AlignHCenter)
            elif newPosicion==2:
                self.txtEdit_respA.setAlignment(Qt.AlignRight)
                self.txtEdit_respB.setAlignment(Qt.AlignRight)
                self.txtEdit_respC.setAlignment(Qt.AlignRight)
                self.txtEdit_respD.setAlignment(Qt.AlignRight)
            self.listBtnPosResp[self.posRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                    f"border-image: url({self.listImagBtnPos[self.posRespuesta]});")
            self.posRespuesta=newPosicion
            self.listBtnPosResp[self.posRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                    f"border-image: url({self.listImagBtnPos[self.posRespuesta]});")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiplesImagen_0()
    application.show()
    app.exec()
    #sys.exit(app.exec())


#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke

# self.btn_pregCen.clicked.connect(lambda: self.editPosPregunta(0))
# self.btn_pregIzq.clicked.connect(lambda: self.editPosPregunta(1))
# self.btn_pregDer.clicked.connect(lambda: self.editPosPregunta(2))