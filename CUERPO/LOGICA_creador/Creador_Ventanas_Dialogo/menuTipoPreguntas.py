from PyQt5 import QtWidgets,Qt
from PyQt5.QtWidgets import QWidget,QLabel,QHBoxLayout
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Main.menuTipoPreguntas_d import Ui_Dialog

###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios


class ImagenClick(QLabel):
    clicked = pyqtSignal(int)
    def __init__(self,idImagen):
        self.idImagen=idImagen
        QtWidgets.QLabel.__init__(self)

    def mousePressEvent(self, event):
        self.clicked.emit(self.idImagen)

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class menuTipoPreguntas(QtWidgets.QDialog, Ui_Dialog):
    usuarioEscogioPregunta=pyqtSignal(int)
    def __init__(self):
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.widgetTipoPreguntas = QWidget()
        self.hbox = QHBoxLayout()
        # imagenes de los iconos
        # Adaptar imagen
        listModalidades = [ RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_BINARIA,
                            RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_MULTIPLE,
                            RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_CHECKBOX,
                            RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_ABIERTA]
        self.listTipoPreguntas=listModalidades

        for i in range(len(listModalidades)):
            pixmapImagen = QPixmap(listModalidades[i]).scaled(65, 65, Qt.KeepAspectRatio,
                                                           Qt.SmoothTransformation)
            object = ImagenClick(i) # i=idPersona...
            object.setStyleSheet("margin: 1px;")
            object.setMinimumSize(70, 70)
            object.setMaximumSize(70, 70)
            object.setPixmap(pixmapImagen)
            object.setStyleSheet("margin:0px; border-radius:5px; border: 1px solid black;")
            object.clicked.connect(self.escogioPregunta)

            # object.setStyleSheet("margin-left: 10px; border-radius: 25px; background: white; color: #4A0C46;");
            self.hbox.addWidget(object)
        self.widgetTipoPreguntas.setLayout(self.hbox)

        # Scroll Area Properties
        self.scroll_visorTipoPreguntas.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_visorTipoPreguntas.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_visorTipoPreguntas.setWidgetResizable(False)
        self.scroll_visorTipoPreguntas.setWidget(self.widgetTipoPreguntas)

        self.setWindowTitle("Tipo de preguntas")

    def escogioPregunta(self,idPersona):
        self.usuarioEscogioPregunta.emit(idPersona)
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = menuTipoPreguntas()
    application.show()
    app.exec()
    #sys.exit(app.exec())

