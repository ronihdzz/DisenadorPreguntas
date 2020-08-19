from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiples_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas



#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from PreguntasMultiplesImagen_0 import PreguntasMultiplesImagen_0
from PreguntasMultiplesImagen_50 import PreguntasMultiplesImagen50
from PreguntasMultiplesImagen_75 import PreguntasMultiplesImagen75
from PreguntasMultiplesImagen_100 import PreguntasMultiplesImagen100
from comporSelect_btnsImagen import comporSelec_btnsImagen
from PyQt5.QtWidgets import  QMessageBox


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiples(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # creando multiples ventanas...
        self.ventanas = []

        self.ventanas.append(PreguntasMultiplesImagen_0())  # pregunta binaria
        self.ventanas.append(PreguntasMultiplesImagen50())  # preguntas multiples
        self.ventanas.append(PreguntasMultiplesImagen75())
        self.ventanas.append(PreguntasMultiplesImagen100())  # preguntas especificas

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()

########################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_hibridasPreg = (self.btn_pregImag0, self.btn_pregImag50, self.btn_pregImag75,
                               self.btn_pregImag100)
        self.listImagen_hibridasPreg=("ICONOS/icon_preg0.png",
                                      "ICONOS/icon_preg50.png",
                                      "ICONOS/icon_preg75.png",
                                      "ICONOS/icon_preg100.png"
                                     )

        self.listNombres_preguntasHibridas=["MUTAPREGIMAG 0%","MUTAPREGIMAG 50%",
                                            "MUTAPREGIMAG 75%", "MUTAPREGIMAG 100%"]

        self.control=comporSelec_btnsImagen(self.listBtnPunteros_hibridasPreg,
                                            self.listImagen_hibridasPreg)
        self.control.COLOR_SELECCION="#D79DDB" #cambiando el color de seleccion
                                               #a uno de color rosa
        self.control.botonFuePresionado.connect(self.cambioHibridoPregunta)
        self.mutacionPregunta=0
        self.control.btnElegido=-1
        self.control.marcarDesmarcarRespuesta_automatico(self.mutacionPregunta,False)
####################################################################################################################
     ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_pregANDpregOR= (self.btn_pregAND,self.btn_pregOR)
        self.listImagen_pregANDpregOR=("ICONOS/icon_and.png",
                                      "ICONOS/icon_or.png",
                                     )
        self.control_2=comporSelec_btnsImagen(self.listBtnPunteros_pregANDpregOR,
                                              self.listImagen_pregANDpregOR)
        #self.control_2.COLOR_SELECCION="#13B470" #cambiando el color de seleccion
                                               #a uno de color rosa
        self.control_2.botonFuePresionado.connect(self.cambio_pregANDpregOR)
        self.pregAND_pregOR=1 #PREGUNTA DEFAULT PREG OR
        self.control_2.btnElegido=-1
        self.control_2.marcarDesmarcarRespuesta_automatico(self.pregAND_pregOR,False)

    def cambio_pregANDpregOR(self,idBtnFuePresionado):
        self.control_2.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)


    def cambioHibridoPregunta(self,idBtnFuePresionado):
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quiere cambiar al formato \n"
                                         f"de pregunta: '{self.listNombres_preguntasHibridas[idBtnFuePresionado]}' ?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.listWidget_panelVersion.setCurrentIndex(idBtnFuePresionado)
            self.control.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiples()
    application.show()
    app.exec()
    #sys.exit(app.exec())


#https://blog.nubecolectiva.com/forma-ideal-de-trabajar-con-imagenes-y-una-base-de-datos-en-un-proyecto-web/

#https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/

#https://stackoverflow.com/questions/3309957/pysqlite-how-to-save-images

#https://www.quora.com/Whats-the-best-way-to-store-images-in-an-SQLite-database-using-Python-Ive-read-that-its-a-bad-idea-to-store-images-in-a-database-however-Im-not-building-a-mass-market-consumer-application-Is-it-a-bad-idea-What-are

