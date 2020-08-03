from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.creadorPreguntasMain_d import  Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from PreguntasEspecificas import PreguntasEspecificas
from PreguntasBinarias import PreguntasBinarias
from PreguntasMultiples import PreguntasMultiples
from PyQt5.QtCore import Qt, pyqtSignal, QFile
from organizacion import constProgram



class BotonChismoso(QPushButton):
    click = pyqtSignal(int)
    def __init__(self,idBoton):
        self.idBoton=idBoton
        QtWidgets.QLabel.__init__(self)

    def mousePressEvent(self, event):
        self.click.emit(self.idBoton)










class evalEqui_1(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons



        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll_barra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setWidget(self.widget)
        self.btn_mas.clicked.connect(self.crearOtraPregunta)


        #creando multiples ventanas...
        self.ventanas={}
        self.ventanas[0]=PreguntasBinarias()
        self.ventanas[1]=PreguntasMultiples()
        self.ventanas[2]=PreguntasEspecificas()
        self.ventanas[3]=PreguntasMultiples() #preguntas codigo

        self.listWidget_panelPreguntas.addWidget(self.ventanas[constProgram.PREG_BINARIAS])
        self.listWidget_panelPreguntas.addWidget(self.ventanas[constProgram.PREG_MULTIPLES])
        self.listWidget_panelPreguntas.addWidget(self.ventanas[constProgram.PREG_ESPECIFICAS])
        self.listWidget_panelPreguntas.addWidget(self.ventanas[constProgram.PREG_CODIGO])


        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelPreguntas.setCurrentIndex(0)
        self.listWidget_panelPreguntas.showFullScreen()


        self.listBotonesPreguntas=[]
        self.contadorPreguntas=0

    def cambioPregunta(self,pregunta):
        print(pregunta)



    def crearOtraPregunta(self):
        self.ventanaMenuPregunta=menuTipoPreguntas()
        self.ventanaMenuPregunta.usuarioEscogioPregunta.connect(self.escogioPregunta)
        self.ventanaMenuPregunta.show()

    def escogioPregunta(self,idPregunta):
        if idPregunta==constProgram.PREG_MULTIPLES:
            self.listWidget_panelPreguntas.setCurrentIndex(idPregunta)
            self.agregarPregunta()

    def agregarPregunta(self):
        object = BotonChismoso(self.contadorPreguntas)
        object.setText(str(self.contadorPreguntas+1))
        object.setStyleSheet("margin: 1px;")
        object.setMinimumSize(50, 50)
        object.setMaximumSize(50, 50)
        object.click.connect(self.cambioPregunta)
        self.vbox.addWidget(object)
        self.contadorPreguntas += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = evalEqui_1()
    application.show()
    app.exec()
    #sys.exit(app.exec())

'''
    
    #https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE


        self.btn_aplicarTam.clicked.connect(self.changedSize)

        self.vSlider_image.sliderMoved.connect(self.changedSizeImage)
        self.btn_mas.clicked.connect(self.crearOtraPregunta)

    def crearOtraPregunta(self):
        self.ventanaMenuPregunta=menuTipoPreguntas()
        self.ventanaMenuPregunta.usuarioEscogioPregunta.connect(self.escogioPregunta)
        self.ventanaMenuPregunta.show()





    def changedSizeImage(self,valor):
        self.txtEdit_preg.setMaximumSize(100,valor*3)
        self.txtEdit_preg.setMinimumSize(100,valor*3)

    def changedSize(self):
        #Cambiando el tamaño
        newTam=self.lineEdit_tamano.text()
        font = QtGui.QFont()
        font.setPointSize(int(newTam))
        self.txtEdit_preg.setFont(font)




'''