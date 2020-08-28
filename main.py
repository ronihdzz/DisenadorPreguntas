from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.CreadorPreguntasMain_d import Ui_MainWindow
from menuTipoPreguntas import menuTipoPreguntas


from PyQt5.QtCore import Qt, pyqtSignal, QFile
from organizacion import constProgram

from PreguntaMultiple import PreguntaMultiple
from PreguntaBinaria import PreguntaBinaria
from PreguntaCheckBox import PreguntaCheckBox
from PreguntaAbierta import PreguntaAbierta
from DataBaseCreadorPreguntas import DataBaseCreadorPreguntas
from PyQt5.QtCore import Qt, pyqtSignal, QFile,QObject
from PyQt5.QtWidgets import  QMessageBox
from Visualizador import VisualizadorPreguntas

class BotonPregunta(QObject):
    suHoraMorir= pyqtSignal(int)#indicara quien es el objeto que quiere morir...
    clickBotonPregunta=pyqtSignal(int)#indicara el id del boton
    def __init__(self,id,botonPregunta,botonMuerte):
        QObject.__init__(self)
        self.id=id #(numeroPregunta,boton)
        self.botonPregunta=botonPregunta
        self.botonMuerte=botonMuerte
        self.botonPregunta.setText(str(self.id+1))

        self.botonMuerte.clicked.connect(self.mandarSenalMuerto)
        self.botonPregunta.clicked.connect(self.darIdBotonPregunta)

        self.COLOR_NORMAL = "#EAE5E5"
        self.COLOR_SELECCION = "#58C3D0"
        self.BORDER_RADIUS = "7"
        self.botonSeleccionado(False)

    def botonSeleccionado(self,botonPresionado):
        if botonPresionado:
            self.botonPregunta.setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                            f"border-radius:{self.BORDER_RADIUS}px;"
                                                            "border: 0.5px solid #555;")
        else:
            self.botonPregunta.setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                            f"border-radius:{self.BORDER_RADIUS}px;"
                                                            "border: 0.5px solid #555;")

    def mandarSenalMuerto(self):
        self.suHoraMorir.emit(self.id)

    def darIdBotonPregunta(self):
        self.clickBotonPregunta.emit(self.id)



class ImagenClick(QLabel):
        clicked = pyqtSignal(int)

        def __init__(self, idImagen):
            self.idImagen = idImagen
            QtWidgets.QLabel.__init__(self)

        def mousePressEvent(self, event):
            self.clicked.emit(self.idImagen)


class CreadorPreguntas(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.nombreCuestionario = "MiCora"
        self.controlABSOLUTO_baseDatos = DataBaseCreadorPreguntas(self.nombreCuestionario)
        self.controlABSOLUTO_baseDatos.crearBaseDatos()
        self.listBotonesPreguntas=[]
        self.listIdPreguntas=[]
        self.punteroPregunta=-1 #numero que no puede ser ningun puntero al incio

        #Acciones del menu...
        self.actionGuardar.setShortcut("Ctrl+g")
        self.actionCrear_nueva_pregunta.setShortcut("Ctrl+p")
        self.actionVisualizar.setShortcut("F5")
        self.actionGuardar.triggered.connect(self.guardarCambios)
        self.actionCrear_nueva_pregunta.triggered.connect(self.crearOtraPregunta)
        self.actionVisualizar.triggered.connect(self.compilarPregunta)


        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll_barra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setWidget(self.widget)
        self.btn_mas.clicked.connect(self.crearOtraPregunta)

        #creando multiples ventanas...
        self.ventanas=[]
        self.ventanas.append( PreguntaBinaria()  )#pregunta binaria
        self.ventanas.append( PreguntaMultiple()  ) #pregunta multiple
        self.ventanas.append( PreguntaCheckBox()  ) #pregunta checbox
        self.ventanas.append( PreguntaAbierta() )#pregunta abierta

        #Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelPreguntas.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelPreguntas.setCurrentIndex(0)
        self.listWidget_panelPreguntas.showFullScreen()

        self.listBotonesPreguntas=[]
        self.contadorPreguntas=0

        self.IMAGEN_ELIMINAR="ICONOS/icon_tache.png"
        self.IMAGEN_ELIMINAR_2="ICONOS/icon_tache2.png"

        self.controlABSOLUTO_visualizador=VisualizadorPreguntas()

    def compilarPregunta(self):
        self.statusbar.showMessage('Compilando pregunta...', 1000)

        widgetPregunta = self.listWidget_panelPreguntas.currentIndex()  # nos dira en que pregunta nos econtramos...

        #self.ventanas[widgetPregunta].listWidget_panelVersion.currentIndex() #nos dira el tipo de respuesta...

        datosPregunta, datosRespueta = self.ventanas[widgetPregunta].getDatos(False)

        self.controlABSOLUTO_visualizador.visualizarPregunta(widgetPregunta,datosPregunta,datosRespueta)
        self.controlABSOLUTO_visualizador.show()


    def guardarCambios(self):
        print("GUARADAR...")
        #mostrando mensaje por 1 segundo
        widgetPregunta=self.listWidget_panelPreguntas.currentIndex() #nos dira en que pregunta nos econtramos...
        datosPregunta,datosRespueta=self.ventanas[widgetPregunta].getDatos()
        print("Datos a guardar...",datosPregunta,datosRespueta)
        idPregunta=self.listIdPreguntas[self.punteroPregunta]
        self.controlABSOLUTO_baseDatos.actualizarDatosPregunta(idPregunta,datosPregunta,datosRespueta)
        self.statusbar.showMessage('Guardando cambios...',1000)

    def cambioPregunta(self,pregunta):
        print(pregunta)

    def crearOtraPregunta(self):
        #mostrando mensaje por 1 segundo
        self.statusbar.showMessage('Creando nueva pregunta...',1000)
        self.ventanaMenuPregunta=menuTipoPreguntas()
        self.ventanaMenuPregunta.usuarioEscogioPregunta.connect(self.escogioPregunta)
        self.ventanaMenuPregunta.show()

    def escogioPregunta(self,tipoRespuesta):
            datosPregunta,datosRespuesta=self.ventanas[tipoRespuesta].preguntaBlanco()
            idNewPregunta=self.controlABSOLUTO_baseDatos.addNewQuestion(tipoRespuesta,datosPregunta,datosRespuesta)
            if idNewPregunta==False:#Si hay un error al crear la pregunta...
                pass
            else:
                self.listWidget_panelPreguntas.setCurrentIndex(tipoRespuesta)
                self.listIdPreguntas.append(idNewPregunta)#agregando el id de la pregunta...
                self.agregarPregunta()

    def verContenidoPregunta(self,idBoton):

        if self.punteroPregunta!=idBoton:
            self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(False)
            self.punteroPregunta=idBoton
            self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(True)

            idPregunta = self.listIdPreguntas[idBoton]
            dataPregunta,dataRespuesta=self.controlABSOLUTO_baseDatos.getData(idPregunta)
            print("ABRIENDO DATOS DE LA PREGUNTA....")
            print(dataPregunta,dataRespuesta)

            #widgetPregunta = self.listWidget_panelPreguntas.currentIndex()  # nos dira en que pregunta nos econtramos...
            tipoRespuesta=dataPregunta["TIPO_RESPUESTA"] #AHI SE ENCUENTRA EL TIPO DE RESPUESTA...
            self.listWidget_panelPreguntas.setCurrentIndex(tipoRespuesta)
            self.ventanas[tipoRespuesta].preguntaBlanco()
            #Eliminamos datos que no necesita...
            del dataPregunta["TIPO_RESPUESTA"]
            del dataPregunta["ID"]
            if tipoRespuesta!=3: #pues las preguntas imagenes no tienen dataRespuesta
                del dataRespuesta["ID"]
            self.ventanas[tipoRespuesta].abrirPregunta(dataPregunta,dataRespuesta)
            #print("Ver pregunta...",idBoton[0])

    def eliminarPregunta(self,posItemMatar):
        self.verContenidoPregunta(posItemMatar)
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quieres\n"
                                         f"eliminar la pregunta numero: {posItemMatar+1}?",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            pass

    def agregarPregunta(self):
        widget = QWidget()
        widget.setMinimumSize(60,75)
        widget.setMaximumSize(60,75)
        gridLayout = QGridLayout(widget)  # Set the checkbox in the layer
        botonCerrar = QPushButton()
        a = "QPushButton{border-image:url(" + self.IMAGEN_ELIMINAR + ");}"
        b = "QPushButton:hover{border-image:url(" + self.IMAGEN_ELIMINAR_2 + ");}"
        c = "QPushButton:pressed{border-image:url(" + self.IMAGEN_ELIMINAR + ");}"
        botonCerrar.setStyleSheet(a + b + c)
        botonCerrar.setMaximumSize(15,15)
        botonCerrar.setMinimumSize(15,15)
        botonPregunta=QPushButton()
        botonPregunta.setMaximumSize(50,50)
        botonPregunta.setMinimumSize(50,50)
        nuevoBotonPregunta=BotonPregunta(self.contadorPreguntas,botonPregunta,botonCerrar)
        self.listBotonesPreguntas.append(nuevoBotonPregunta)
        nuevoBotonPregunta.clickBotonPregunta.connect(self.verContenidoPregunta)
        nuevoBotonPregunta.suHoraMorir.connect(self.eliminarPregunta)
        nuevoBotonPregunta.darIdBotonPregunta()  # hacer como que lo selecciona...


        # addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        gridLayout.addWidget(botonCerrar, 0, 0, 1, -1, alignment=QtCore.Qt.AlignRight)
        gridLayout.addWidget(botonPregunta,1, 0, -1, -1,alignment=QtCore.Qt.AlignHCenter)
        gridLayout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding
        self.vbox.addWidget(widget,alignment=QtCore.Qt.AlignHCenter)
        self.contadorPreguntas += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CreadorPreguntas()
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





'''