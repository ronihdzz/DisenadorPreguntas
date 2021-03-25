from PyQt5.QtWidgets import QDialog
import sys, re
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Ejecutador.ConfirmacionAccion_d import Ui_Dialog

###############################################################
#  MIS LIBRERIAS...
##############################################################

class ConfirmadorAccion(QDialog, Ui_Dialog):
    # Metodo constructor:
    accionConfirmada = pyqtSignal(bool) #dira si la accion se confirmo bien...

    def __init__(self,indicaciones="",palabraConfirmacion=""):
    #def __init__(self,parent=None):
        #super(EditarNombre, self).__init__(parent)  # propiedad para ser segunda ventana
        Ui_Dialog.__init__(self)
        QDialog.__init__(self)
        self.setupUi(self)

        # Como manipular nuestro lineEdit cada ves
        # que se introduzcan letras
        #self.lineEdit_nombre.textChanged.connect(self.validar_nombre)
        self.indicaciones=indicaciones
        self.palabraConfirmacion=palabraConfirmacion

        self.textEdit_indicaciones.setText(self.indicaciones)
        self.textEdit_indicaciones.setReadOnly(True)

        self.lineEdit_wordRepetir.setText(self.palabraConfirmacion)
        self.lineEdit_wordRepetir.setReadOnly(True)

        self.lineEdit_firma.textChanged.connect(self.validarFirma)

        self.btn_aceptar.clicked.connect(self.concretarAccion)

        self.firmaEscritaCorrectamente =False

        self.validarFirma()#para que se ponga en rojo...


    def concretarAccion(self):
        if self.palabraConfirmacion!=self.lineEdit_firma.text():
            QMessageBox.critical(self, "Atencion", "Las palabras no coinciden", QMessageBox.Ok)
        else:
            resultado = QMessageBox.warning(self,"Atencion",f"¿Estas seguro de lo que haras?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.firmaEscritaCorrectamente=True
                self.close()

    # primer metodo para validar el dato nombre
    def validarFirma(self):
        if self.palabraConfirmacion!=self.lineEdit_firma.text():  # si la validacion no es correcta  (si  no es True)
            # modifcando el estilo del objeto etiqueta llamado 'nombre'
            self.lineEdit_firma.setStyleSheet("border-radius:5px; border:5px solid red;")
        else:  # no pasa ningun error
            self.lineEdit_firma.setStyleSheet("border-radius:5px; border: 5px solid green;")

    def closeEvent(self, event):
        if self.firmaEscritaCorrectamente:
            self.accionConfirmada.emit(True) # mandando nombre
            event.accept()  # Saldremos del evento
        else:
            resultado = QMessageBox.question(self, "Salir ...",
                                             "¿Seguro que quieres salir?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()  # No saldremos del evento

########################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = ConfirmadorAccion("BLABLABLABLABLA","acepto los terminos")
    dialogo.show()
    app.exec_()

