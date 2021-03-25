from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox

from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_InteractuadorServidor.InteractuadorMain import Ui_Form
from CUERPO.LOGICA_creador.Creador_InteractuadorLocal.InteractuadorCuestionarios import InteractuadorCuestionarios
from CUERPO.LOGICA_creador.Creador_InteractuadorServidor.InteractuadorDescargas import InteractuadorParaDescargarCuestionarios
from CUERPO.LOGICA_creador.Creador_InteractuadorServidor.InteractuadorCompartidos import InteractuadorCuestionariosCompartidos



###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################



class InteractuadorMain(QWidget,Ui_Form):
    senalTestCompartido = pyqtSignal(bool)
    def __init__(self,nombreUsuario=""):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        self.nombreUsuario=nombreUsuario

        self.ventanaCuestionarios=InteractuadorCuestionarios(nombreUsuario=self.nombreUsuario)
        self.ventanaCuestionarios.senalCuestionarioCompartido.connect(self.abrirCuesitonarioCompartidos)
        self.ventanaCuestionarios.senalTestCompartido.connect(lambda x: self.senalTestCompartido.emit(True) )


        self.ventanaCompartidos=InteractuadorCuestionariosCompartidos(nombreUsuario=self.nombreUsuario)
        self.ventanaCompartidos.senalCuestionarioDescargado.connect(self.abrirVentanaCuestionariosDescargados)


        self.ventanaDescargas=InteractuadorParaDescargarCuestionarios()
        self.ventanaDescargas.senalCuestionarioDescargado.connect(self.abrirVentanaCuestionariosDescargados)


        self.tabWidget.addTab(self.ventanaCuestionarios,"Cuestionarios")
        self.tabWidget.addTab(self.ventanaCompartidos, "Compartidos")
        self.tabWidget.addTab(self.ventanaDescargas,"Descargar")

    def abrirCuesitonarioCompartidos(self,estado):
        self.ventanaCompartidos.refrescarCompartidos()
        self.tabWidget.setCurrentIndex(1)#0==>cuestionarios,1==>compartidos,2==>descargas

    def abrirVentanaCuestionariosDescargados(self):
        self.tabWidget.setCurrentIndex(0)#0==>cuestionarios,1==>compartidos,2==>descargas
        self.ventanaCuestionarios.refrescarDatosCuestionarios(descargas=True)
        # abrimos el apartado de los cuestionarios descargados...
        self.ventanaCuestionarios.controlABSLUTO_tipoCuestionarios.botonPresionado(1)





if __name__ == '__main__':
    app = QApplication([])
    application = InteractuadorMain(nombreUsuario="Roni")
    application.show()
    app.exit(app.exec())