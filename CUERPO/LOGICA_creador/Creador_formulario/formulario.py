from PyQt5 import QtWidgets
import sys
from os import getcwd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QFileDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QThread  # hilos

from PyQt5.QtWidgets import QDialog, QCompleter
from functools import partial

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QDoubleValidator,QRegExpValidator


###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_InicioSesion.registro_d import Ui_Dialog
from CUERPO.LOGICA_creador.Creador_ClasesOrden.ClaseOrden_0 import ClaseOrden_0
from CUERPO.LOGICA_creador.Creador_ClasesOrden.ClaseOrden_2 import ClaseOrden_2
from CUERPO.LOGICA_creador.Creador_formulario.DataBase_formulario import DataBase_formulario

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################


class Formulario(QtWidgets.QDialog, Ui_Dialog):
    # las siguientes constantes almacenan los nombres de las imagenes que cambiaran en función
    # del comportamiento de cada boton...
    IMAGEN_OJO_VER = "border-image: url(:/prefijoNuevo/IMAGENES_creador/eyes_off.png);"
    IMAGEN_OJO_NO_VER = "border-image: url(:/prefijoNuevo/IMAGENES_creador/eyes_on.png);"

    IMAGEN_MAL = '''QPushButton{border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_0.png);}
                  QPushButton:hover{ border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_1.png);}
                  QPushButton:pressed{border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_2.png);}'''
    IMAGEN_BIEN = '''QPushButton{border-image:url(:/prefijoNuevo/IMAGENES_creador/paloma_0.png);}
                  QPushButton:hover{ border-image:url(:/prefijoNuevo/IMAGENES_creador/paloma_1.png);}
                  QPushButton:pressed{border-image:url(:/prefijoNuevo/IMAGENES_creador/paloma_2.png);}'''

    TUPLA_RESOLUCION_DUDAS = (

        '''Restricciones:
Cada campo tiene sus propias restricciones, 
para poder verlas debes dar click en el 
boton que tiene forma de tache o  paloma,
este boton se encuentra a lado derecho de
cada campo.''',

        '''El nombre de usuario:
    -Solo puede ser una palabra.
    -Solo puede estar conformado de
    letras minusculas y numeros.
    -No debe coincidir con los 
    nombres ya existentes:''',

        '''La edad:
    -La edad minima que debes tener
    son 4 años.''',

        '''La contraseña:
    -Su unica restricción es que no 
    debe tener espacios en blanco.''',

        '''La repetición de contraseña:
    -Debe ser exactamente la misma que 
    la contraseña.''',

        '''Nombre de mejor amigo:
    -Solo puede ser una palabra.
    -Solo puede estar conformado de
    letras minusculas.'''
    )

    senalUsuarioCerro=pyqtSignal(bool)
    senalUsuarioSeRegistro=pyqtSignal(list)



    def __init__(self,listaNombreUsuarios=[]):

        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.listaNombreUsuarios=listaNombreUsuarios

        self.agruparVariablesInstancia()
        self.conectarObjetos_conMetodos()
        self.restringirLasEntradas()

        self.USUARIO_SE_REGISTRO=False

#############################################################################################################################################
#        A C C I O N E S    F R E  C U E N  T E S :
#############################################################################################################################################
    def verNoVer_contenido(self, idObjeto):
        le = self.tupla_leVerNoVer[idObjeto]
        bo = self.tupla_btnVerNoVer[idObjeto]

        if le.echoMode() == QLineEdit.Password:
            le.setEchoMode(QLineEdit.Normal)
            bo.setStyleSheet(self.IMAGEN_OJO_VER)
        else:
            le.setEchoMode(QLineEdit.Password)  # ponemos los puntos negros
            bo.setStyleSheet(self.IMAGEN_OJO_NO_VER)  # cambiamos a la imagen de ojo no ver...

    def informar(self,idDuda):
        '''
        Lo que hace esta funcion es que en funcion del boton de estado que
        se oprima se mostrara la restriccion de su apartado...
        '''
        mensaje = self.TUPLA_RESOLUCION_DUDAS[idDuda]
        if idDuda==1: #si el id de la duda es del nombre de usuario
           mensaje+= ( "\n\t-" + "\n\t-".join(self.listaNombreUsuarios) )

        QMessageBox.information(self, ClaseOrden_0.NOMBRE_APLICACION,mensaje,
                             QMessageBox.Ok)

    def validarEntradas(self, id_le):
        '''
        Lo que hara el siguiente metodo es validar los datos que el usuario ingresa
        cuando esta escribiendo, si los datos son correctos lo indicaremos con un
        booleano
        '''

        # ¿el dato que se modifico fue la contraseña o la repeticion de la contraseña?
        if self.dict_datosPediremos[id_le][0] == self.le_password_2 or self.dict_datosPediremos[id_le][0] == self.le_password_1:  # si no es la repetición de la contraseña

            # cualquier dato que se haya modificado no podemos poner algo bien
            # si la contraseña ES NADA
            if self.le_password_1.text() == "":
                self.dict_btnEstadoAviso[3].setStyleSheet(self.IMAGEN_MAL)
                self.dict_btnEstadoAviso[4].setStyleSheet(self.IMAGEN_MAL)

                self.dict_datosPediremos[3][1] = False
                self.dict_datosPediremos[4][1] = False


            else:  # si resulta que la contraseña es diferente de nada:
                # vamos a checar si la repeticion de esta esta bien....
                self.dict_btnEstadoAviso[3].setStyleSheet(self.IMAGEN_BIEN)
                self.dict_datosPediremos[3][1] = True

                if self.le_password_2.text() == self.le_password_1.text():
                    self.dict_btnEstadoAviso[4].setStyleSheet(self.IMAGEN_BIEN)
                    self.dict_datosPediremos[4][1] = True
                else:
                    self.dict_btnEstadoAviso[4].setStyleSheet(self.IMAGEN_MAL)
                    self.dict_datosPediremos[4][1] = False

        # si el dato que se modifico no fue la contraseña ni su repeticion...
        # checaremos si se trata del nombre de usuario...
        elif self.dict_datosPediremos[id_le][0] == self.le_nameUser:  # si el dato que se esta modificando
            # es el nombre de usuario debemos preguntar
            # lo siguiente...
            if self.le_nameUser.text() in self.listaNombreUsuarios or self.le_nameUser.text() == "":
                self.dict_btnEstadoAviso[id_le].setStyleSheet(self.IMAGEN_MAL)
                self.dict_datosPediremos[id_le][1] = False
            else:
                self.dict_btnEstadoAviso[id_le].setStyleSheet(self.IMAGEN_BIEN)
                self.dict_datosPediremos[id_le][1] = True

        else:
            if self.dict_datosPediremos[id_le][0].text() != "":
                self.dict_btnEstadoAviso[id_le].setStyleSheet(self.IMAGEN_BIEN)
                self.dict_datosPediremos[id_le][1] = True
            else:
                self.dict_btnEstadoAviso[id_le].setStyleSheet(self.IMAGEN_MAL)
                self.dict_datosPediremos[id_le][1] = False

#############################################################################################################################################
#         A G R U P A C I O  N  E S     D  E    L O S    A T R I B U T O S    Y   C O N E X I O  N  E S    :
#############################################################################################################################################
    def agruparVariablesInstancia(self):
        # La siguiente tupla almacena los mensajes de las restricciones de cada
        # campo:


        # El siguiente diccionario almacena los punteros de los objetos botones
        # que se encuentran a lado de cada seccion,esos botones son los
        # tienen imagen de tache o palomo. La finalidad del diccionario
        # es conectar todos los botones de una manera mas sencilla:
        self.dict_btnEstadoAviso = {
            0: self.btn_infoDudas,
            1: self.btn_nameUser,
            2: self.btn_edad,
            3: self.btn_password_1,
            4: self.btn_password_2,
            5: self.btn_mejorAmigo
        }
        # El siguiente diccionario almacena los line edit en donde el usuario
        # tiene que ingresar sus datos, y donde este puede tener una mal
        # sintaxis, por tal motivo cada value es una lista de un objeto line edit
        # y un booleano que indicara si es buena o mala su sintaxis
        # otra cosa que aclara es que su keys coincide con la key del su boton estado
        self.dict_datosPediremos = {1: [self.le_nameUser, False],
                                    3: [self.le_password_1, False],
                                    4: [self.le_password_2, False],
                                    5: [self.le_nameFriend, False]
                                    }
        # almacenara los botones de forma de ojo en una tupla para que se mas facil
        # ponerles el mismo comportamiento de ver o no ver contraseña a todos al mismo tiempo
        self.tupla_btnVerNoVer = (self.btn_mostrarPassword_1, self.btn_mostrarPassword_2, self.btn_mostrarMejorAmigo)
        self.tupla_leVerNoVer = (self.le_password_1, self.le_password_2, self.le_nameFriend)

    def conectarObjetos_conMetodos(self):
        # Si detecta algun cambio en el texto veremos si ya es el correcto...
        for x in tuple(self.dict_datosPediremos.keys()):
            self.dict_datosPediremos[x][0].textChanged.connect(partial(self.validarEntradas, x))

        # en funcion del boton estado que se presione mostraremos su respectivo mensaje...
        for x in tuple(self.dict_btnEstadoAviso.keys()):
            self.dict_btnEstadoAviso[x].clicked.connect(partial(self.informar, x))

        for x in range(len(self.tupla_btnVerNoVer)):
            self.tupla_btnVerNoVer[x].clicked.connect(partial(self.verNoVer_contenido, x))
            self.tupla_btnVerNoVer[x].click()

        self.btn_terminarRegistro.clicked.connect(self.terminarRegistro)

    def restringirLasEntradas(self):

        # validacion del nombre de usuario...
        validator = QRegExpValidator(QRegExp("[0-9a-z]{1,15}"))  # maximo solo 15 caracteres
        self.le_nameUser.setValidator(validator)

        # validacion del nombre del mejor amigo...
        validator = QRegExpValidator(QRegExp("[a-z]{1,15}"))  # maximo solo 15 caracteres
        self.le_nameFriend.setValidator(validator)

        # validacion de la contraseña...
        validator = QRegExpValidator(QRegExp("[^ ]{1,15}"))  # maximo solo 15 caracteres
        self.le_password_1.setValidator(validator)
        self.le_password_2.setValidator(validator)



#############################################################################################################################################
#      A C C I O N E S     F I N A L E S :
#############################################################################################################################################

    def terminarRegistro(self):
            datosCorrectos = True
            # Con que haya uno malo el resultado sera false...
            print("\n" * 4)
            for x in tuple(self.dict_datosPediremos.keys()):
                datosCorrectos *= self.dict_datosPediremos[x][1]
                print(f"{x} = {self.dict_datosPediremos[x][1]}")

            if datosCorrectos:
                resultado = QMessageBox.question(self, ClaseOrden_0.NOMBRE_APLICACION,
                                                 "¿Seguro que los datos proporcionados\n"
                                                 "son los datos correctos?",
                                                 QMessageBox.Yes | QMessageBox.No)
                if resultado == QMessageBox.Yes:
                    mensajeBienvenida = '''
    Felicidades, tus datos han sido registrados
    exitosamente,ya puedes hacer uso de tu cuenta.'''
                    QMessageBox.information(self, ClaseOrden_0.NOMBRE_APLICACION,
                                            mensajeBienvenida,
                                            QMessageBox.Ok)
                    self.USUARIO_SE_REGISTRO=True
                    self.close()

            else:
                mensajeError = '''El registro no se puede realizar porque:
    tienes errores en los datos requeridos.
    Por favor respeta las restricciones de 
    cada campo,si tienes dudas acerca de 
    cuales son, da click en el boton que
    tiene forma de tache o paloma, el cual
    se encuentra al lado derecho de cada 
    campo.'''
                QMessageBox.critical(self, ClaseOrden_0.NOMBRE_APLICACION,
                                     mensajeError,
                                     QMessageBox.Ok)


    def closeEvent(self, event):

        if self.USUARIO_SE_REGISTRO:
            nameUser=self.le_nameUser.text()
            edad=self.sB_edad.value()
            contrasena=self.le_password_1.text()
            mejorAmigo=self.le_nameFriend.text()
            self.senalUsuarioSeRegistro.emit([nameUser,edad,contrasena,mejorAmigo])
            event.accept()

        else:

            mensage='''¿En verdad deseas salir?
Si sales tus datos ingresados 
se perderan'''
            resultado = QMessageBox.question(self,ClaseOrden_0.NOMBRE_APLICACION,
                                             mensage,
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                event.accept()
                self.senalUsuarioCerro.emit(True)
            else:
                event.ignore()  # No saldremos del evento


if __name__ == "__main__":
    # Cambiando de direcciones sus carpetas u archivos...
    app = QtWidgets.QApplication([])
    application = Formulario(listaNombreUsuarios=["roni99","jorge","dilan"])
    application.show()
    sys.exit(app.exec())






