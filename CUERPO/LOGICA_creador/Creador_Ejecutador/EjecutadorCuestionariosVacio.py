from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Ejecutador.EjecutadorCuestionarioVacio_d import Ui_Form
###############################################################
#  MIS LIBRERIAS...
##############################################################


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class EjecutadorCuestionariosVacios(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = EjecutadorCuestionariosVacios()
    application.show()
    app.exec()
    #sys.exit(app.exec())