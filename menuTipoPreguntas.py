from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...
from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.menuTipoPreguntas_d import Ui_Dialog
from PyQt5.QtCore import Qt, pyqtSignal, QFile
from PyQt5.QtWidgets import  QMessageBox



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
        listModalidades = ["modalidad1_trueFalse.png", "modalidad2_cualDeTodas.png", "modalidad3_cualesSon.png",
                           "modalidad5_programacion"]
        self.listTipoPreguntas=listModalidades

        for i in range(len(listModalidades)):
            pixmapImagen = QPixmap("IMAGENES/"+listModalidades[i]).scaled(65, 65, Qt.KeepAspectRatio,
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

    def escogioPregunta(self,idPersona):
        self.usuarioEscogioPregunta.emit(idPersona)
        print(idPersona)
        self.close()

        '''
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "Escogiste el tipo de pregunta: \n"
                                         f" -{self.listTipoPreguntas[idPersona]} \n"
                                         " ¿Estas seguro?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.usuarioEscogioPregunta.emit(idPersona)
            print(idPersona)
            self.close()
        else:
            print("hola")     
        '''





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = menuTipoPreguntas()
    application.show()
    app.exec()
    #sys.exit(app.exec())

