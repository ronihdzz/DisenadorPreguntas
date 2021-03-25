from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox

from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_TestDelphia.TestDelphiaMain_d import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_TestDelphia.TestOriginales import TestOriginales
from CUERPO.LOGICA_creador.Creador_TestDelphia.TestDescargar import TestDescargar

class TestDelphiaMain(QWidget,Ui_Form):
    senalTestDescargado = pyqtSignal(bool)  # comunicacion con la aplicacionn
    def __init__(self,nombreUsuario=""):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        self.nombreUsuario=nombreUsuario

        self.ventana_testOriginales=TestOriginales(nombreUsuario=self.nombreUsuario)
        self.ventana_descargarTest = TestDescargar(self.nombreUsuario)


        self.tabWidget.addTab(self.ventana_testOriginales,"Originales")
        self.tabWidget.addTab(self.ventana_descargarTest,"Descargar")

        #actualizamos los test de la tabla de descargas...
        self.ventana_testOriginales.senalActualizacionTest.connect(lambda x: self.ventana_descargarTest.mostrarTablaCuestionarios())

        self.ventana_descargarTest.senalTestDescargado.connect(lambda x: self.senalTestDescargado.emit(True))


if __name__ == '__main__':
    app = QApplication([])
    application = TestDelphiaMain(nombreUsuario="Roni")
    application.show()
    app.exit(app.exec())