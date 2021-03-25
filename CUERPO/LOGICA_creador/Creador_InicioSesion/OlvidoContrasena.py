from PyQt5.QtWidgets import QDialog
import sys, re
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_InicioSesion.olvidoContrasena_d import Ui_Dialog

###############################################################
#  MIS LIBRERIAS...
##############################################################

class OlvidoContrasena(QDialog, Ui_Dialog):
    # Metodo constructor:
    #accionConfirmada = pyqtSignal(bool) #dira si la accion se confirmo bien...

    def __init__(self,mejorAmigo=""):
        mensaje=f'''Hola:{mejorAmigo}, no te preocupes si has 
olviado tu contraseña, podras entrar a tu cuenta ingresando el 
nombbre de tu mejor amigo.'''.replace("\n","")


        Ui_Dialog.__init__(self)
        QDialog.__init__(self)
        self.setupUi(self)

        self.bel_mensaje.setText(mensaje)



########################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = OlvidoContrasena("Sebastian")
    dialogo.show()
    app.exec_()

