from PyQt5 import QtWidgets
import sys
from os import getcwd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QFileDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QThread  # hilos

from PyQt5.QtWidgets import QDialog,QCompleter

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_InicioSesion.inicioSesion_d import Ui_Dialog

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_InteractuadorLocal.InteractuadorCuestionarios import InteractuadorCuestionarios

from CUERPO.LOGICA_creador.Creador_formulario.DataBase_formulario import DataBase_formulario
from CUERPO.LOGICA_creador.Creador_ClasesOrden.ClaseOrden_0 import ClaseOrden_0
from CUERPO.LOGICA_creador.Creador_formulario.formulario import Formulario




class inicioSesion(QtWidgets.QDialog,Ui_Dialog):
    # las siguientes constantes almacenan los nombres de las imagenes que cambiaran en función
    # del comportamiento de cada boton...
    IMAGEN_OJO_VER = "border-image: url(:/prefijoNuevo/IMAGENES_creador/eyes_off.png);"
    IMAGEN_OJO_NO_VER = "border-image: url(:/prefijoNuevo/IMAGENES_creador/eyes_on.png);"


    def __init__(self):
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        # CONFIGRUACION DEL COMBOX PARA FACILITAR LA BUSQUEDA DE AUTORES DE CUESTIONARIOS..
        # ACCEDIENDO A LA BASE DE DATOS
        self.DATA_BASE = DataBase_formulario(ClaseOrden_0.BASE_DATOS_DATOS_GENERALES)
        self.DATA_BASE.crearBaseDatos()

        self.conectar_Aobjetos()
        self.cargarNombresUsuario()

        #lo siguiente lo hacemos para que se cargue la foto de perfil
        #del usuario numero cero...
        if self.noUserRegis > 0:
            self.comBox_nombres.setCurrentIndex(0)

        #lo siguiente lo hacemos para que se cargue la foto del boton de
        #motrar/oculta contraseña
        self.btn_mostrarPassword.click()

#######################################################################################################################################
#        P  R   E   P   A   R   A   T   I   V   O   S   :
#######################################################################################################################################

    def conectar_Aobjetos(self):
        '''
        La siguiente función tiene como objetivo conectar las funciones
        con determinadas señales de los objetos
        '''

        self.comBox_nombres.currentIndexChanged.connect(self.eligioUnUsuario)
        self.btn_registrar.clicked.connect(self.crearCuenta)
        self.btn_mostrarPassword.clicked.connect(self.verNoVer_contenido)
        self.btn_iniciarSesion.clicked.connect(self.validarUsuario)

    def cargarNombresUsuario(self):
        '''
        La siguiente función hara una consulta a la base de datos
        para cargar los datos de los usuarios, asi como tambien
        carcagara los nombres en el combo box y configurara al combo
        box para que sea mas ameno elgegir el nombre del usuario
        '''

        #obteniendo de la base de datos los datos de todos los usuarios
        #pero unicamente su clave y foto de perfil....
        self.dictUsuarios = self.DATA_BASE.getAll_datos(CLAVE=True, FOTO_PERFIL=True)


        #esto es importante porque la utiliza el ComboBox para el QCompleter:
        self.listaUsuarios = list(self.dictUsuarios.keys())

        #Las siguientes propiedades son importantes definir por que las utiliza  el QCompleter...
        self.noUserRegis=len(self.listaUsuarios) #numero de usuarios registrados
        self.indexUserChoose=-1 #indice del usuario elegido

        # C O M B O     B O X   ==>dandole la propiedad de QAcompleter...
        self.comBox_nombres.clear()
        acompletador = QCompleter(self.listaUsuarios)
        acompletador.setCaseSensitivity(Qt.CaseInsensitive)
        self.comBox_nombres.setEditable(True)
        self.comBox_nombres.addItems(self.listaUsuarios)
        self.comBox_nombres.setCompleter(acompletador)




#######################################################################################################################################
#       M   E   T   O   D   O   S       :
#######################################################################################################################################

    def verNoVer_contenido(self):
        '''
        Este metodo es el metodo al cual ira conectado el boton
        que permite ver o encriptar lo que estas escribiendo
        en el line edit de la contraseña.Otra cosa que hace este
        metodo es cambiar la imagen de dicho boton, para que se
        vea la diferencia de cuando se ve o no la contraseña
        '''

        if  self.edit_clave.echoMode() == QLineEdit.Password:
            self.edit_clave.setEchoMode(QLineEdit.Normal)
            self.btn_mostrarPassword.setStyleSheet(self.IMAGEN_OJO_VER)
        else:
            self.edit_clave.setEchoMode(QLineEdit.Password)
            self.btn_mostrarPassword.setStyleSheet(self.IMAGEN_OJO_NO_VER)

    def eligioUnUsuario(self,index):
        '''
        Este es un metodo al cual va conectado el combo box, y el cual
        tiene como principal objetivo borrar los items que el usuario
        genere cuando escriba nombres que no estan definidos en la lista
        de usuarios.
        Otro objetivo de este metodo es cambiar la imagen de la label de foto
        de perfil, cada vez que el usuario elige otro usuario...
        '''
        if index>=self.noUserRegis:
            QMessageBox.critical(self, "Atencion",
                                 "No existe usuario cuyo \n"
                                 f"nombre sea:{self.comBox_nombres.currentText()}",
                                 QMessageBox.Ok)
            self.comBox_nombres.removeItem(index)
        elif self.indexUserChoose!=index: #eligio a uno  diferente,,,

            namePersonQuiereEntrar = str(self.comBox_nombres.currentText())
            imagen=ClaseOrden_0.direc_FotosUsuario+self.dictUsuarios[namePersonQuiereEntrar]['FOTO_PERFIL']

            pixmapImagen = QPixmap(imagen).scaled(self.bel_fotoPerfil.size(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
            # Mostrar imagen por medio de los punteros labels...
            self.bel_fotoPerfil.setAlignment(Qt.AlignCenter)
            self.bel_fotoPerfil.setPixmap(pixmapImagen)

            self.indexUserChoose=index


    def crearCuenta(self):
        '''
        Lo que hara este metodo es llamar la ventana de registro, con la finalidad
        de atender la peticion del usuario de quererse registrar...
        '''
        self.formulario=Formulario(self.listaUsuarios)

        self.formulario.senalUsuarioCerro.connect(self.volverMostraInicioSesion)
        self.formulario.senalUsuarioSeRegistro.connect(self.registrarRegistroExitoso)
        self.hide()
        self.formulario.show()


    def registrarRegistroExitoso(self,listDatos):
        '''
        Una vez que el usuario se registro exitosamente, automaticamente
        este metodo abrira la ventana del menu de cuestionarios,y tambien
        registrara sus datos en la base de datos y por ende
        debera actualizar el nuevo valor el el combo box
        '''
        self.DATA_BASE.addUsuario(NOMBRE_USUARIO=listDatos[0],EDAD=listDatos[1],
                                  CLAVE=listDatos[2],AMIGO=listDatos[3],
                                  FOTO_PERFIL=ClaseOrden_0.IMAGEN_DEFAULT_USUARIO)

        nombrePersona=listDatos[0]

        self.cargarNombresUsuario()

        if self.noUserRegis > 0:
            self.comBox_nombres.setCurrentIndex(0)

        self.abrirMain(nombrePersona)


    def abrirMain(self,nombrePersona):
        '''
        Lo que hara el siguiente metodo es abrir la cuenta de cuestionarios
        del usuario, pues este metodo se llama cuando el usuario a ingresado
        su contraseña correcta...
        '''
        RecursosCreadorCuestionarios.cambiarDireccion("RECURSOS/",nombrePersona)
        self.ventanaMain=InteractuadorCuestionarios(nombreUsuario=nombrePersona)
        self.ventanaMain.senalUsuarioCerro.connect(self.volverMostraInicioSesion)
        self.ventanaMain.show()

    def volverMostraInicioSesion(self):
        self.show()


    def validarUsuario(self):
        '''
        El siguiente metodo tiene la finalidad de evaluar si la contraseña
        escrita por el usuario es la correcta o no.
        '''
        namePersonQuiereEntrar = str(self.comBox_nombres.currentText())
        password = self.edit_clave.text()
        try:
            if password==self.dictUsuarios[namePersonQuiereEntrar]['CLAVE']:
                self.hide()
                self.abrirMain(namePersonQuiereEntrar)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Contraseña incorrecta, vuelve a intentarlo.")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
        except:
            QMessageBox.critical(self, "Atencion",
                                 "No existe usuario cuyo \n"
                                 f"nombre sea:{namePersonQuiereEntrar}",
                                 QMessageBox.Ok)


#############################################################################################################################################
#      A C C I O N E S     F I N A L E S :
#############################################################################################################################################

    def closeEvent(self, event):
            resultado = QMessageBox.question(self, "RonTest",
                                             "¿Seguro que quieres salir?\n",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()  # No saldremos del evento




if __name__ == "__main__":
    #Cambiando de direcciones sus carpetas u archivos...
    ClaseOrden_0.cambiarDireccion("RECURSOS/")
    app = QtWidgets.QApplication([])
    application = inicioSesion()
    application.show()
    sys.exit(app.exec())

#https://www.w3schools.com/css/css_font_size.asp
