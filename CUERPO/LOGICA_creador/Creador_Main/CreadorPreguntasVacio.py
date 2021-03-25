from PyQt5 import QtWidgets

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Main.CreadorPreguntasVacio_d import Ui_Form

###############################################################
#  MIS LIBRERIAS...
##############################################################


class CreadorPreguntasVacio(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CreadorPreguntasVacio()
    application.show()
    app.exec()
    #sys.exit(app.exec())