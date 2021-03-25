#documentacion...
#https://cloud.google.com/storage/docs/deleting-objects#storage-delete-object-python
from CUERPO.LOGICA_creador.Creador_MisPaquetes.FuncionesStorageFirebase import FuncionesStorageFirebase
from PyQt5.QtWidgets import QDialog
import sys, re
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
import random  #numeros aleatorios
from datetime import datetime#para poner el nombre de la fecha
from google.cloud import storage
import shutil
import os
from datetime import datetime




#Para poder usar esta clase primero debemos iniciar la comunicacion...
from CUERPO.LOGICA_creador.Creador_MisPaquetes import FuncionesCompresion
import pyrebase

from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi

class FirebaseCuestionarios():
    def __init__(self,context):
        self.context = context


    def mensajeEmergenteError(self):
        QMessageBox.critical(self.context, "Error de red con el servidor",
                             "Lo sentimos, ocurrio un error\n"
                             "intentalo de nuevo pero procura\n"
                             " tener acceso a internet porque\n"
                             "probablemene el error ocurrio por falta de\n "
                             "conexion",
                             QMessageBox.Ok)

    def iniciarComunicacion(self,mensajeActivado=True):
        try:
            # Configuración Pyrebase
            configuracion = {
                "apiKey": "AIzaSyCdVBUZ73YjC04yONZLTiLcpvnSlbWuHs4",
                "authDomain": "delphiadata.firebaseapp.com",
                "databaseURL": "https://delphiadata.firebaseio.com",
                "projectId": "delphiadata",
                "storageBucket": "delphiadata.appspot.com",
                "messagingSenderId": "319244349329",
                "appId": "1:319244349329:web:4aa5e609d50c8054d1f430",
                "measurementId": "G-W0FZZKMMS6"}
            self.pyBase = pyrebase.initialize_app(configuracion)
            self.db = self.pyBase.database()
            return True
        except:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None

    def getAllCalifTest(self,nombreUsuario,mensajeActivado=True):
        operacionExitosa=True
        listDatos_tests = CuestionariosDelphi.getNombresCuestionarios(oficiales=True)
        nombresTest=[x["NOMBRE"] for x in listDatos_tests]
        print("ajajjajajajajajaj",nombresTest)
        listCalif=[]
        for test in nombresTest:
            try:
              #si no existe ese dato retornara un None
              a=self.db.child("TEST_DELPHIA").child(test).child(nombreUsuario).child("CALIF").get().val()
              if a==None:
                a=0
                listCalif.append(a)
              else:
                listCalif.append(a)
            except:
                operacionExitosa=False
                break

        if operacionExitosa:
            return tuple(listCalif)
        else:
            self.mensajeEmergenteError()
            return None

    def subirCalifTest(self,nombreUsuario,nombreTest,calif,mensajeActivado=True):
        operacionExitosa = True
        try:
            self.db.child("TEST_DELPHIA").child(nombreTest).child(nombreUsuario).child("CALIF").set(calif)
        except:
            operacionExitosa = False

        if operacionExitosa:
            QMessageBox.critical(self.context, "Felicidades n.n",
                                 "Calificacion subida a la base\n"
                                 "de datos con,exito rotundo.",
                                 QMessageBox.Ok)
            return True
        else:
            self.mensajeEmergenteError()
            return None

    def subirCalifCampechano(self,nombreUsuario,calif):
        nombreDefault=self.getNameDefault() #Nombre que sera default...
        operacionExitosa = True

        data={"CALIF":calif}
        try:
            self.db.child("TEST_DELPHIA").child("CAMPECHANO").child(nombreUsuario).child(nombreDefault).set(data)
        except:
            operacionExitosa = False

        if operacionExitosa:
            QMessageBox.critical(self.context, "Felicidades n.n",
                                 "Calificacion subida a la base\n"
                                 "de datos con,exito rotundo.",
                                 QMessageBox.Ok)
            return True
        else:
            return None

    def getNameDefault(self):
        now = datetime.now()
        # Tiempo apartir del 2020 cuando inicio el juego
        secondYears_50 = 50 * 365 * 24 * 60 * 60
        timeApartir2020 = now.timestamp() - secondYears_50
        redondeo_4 = int(timeApartir2020 * 1000.0)
        return str(redondeo_4)

'''
# Configuración Pyrebase
configuracion = {
    "apiKey": "AIzaSyCdVBUZ73YjC04yONZLTiLcpvnSlbWuHs4",
    "authDomain": "delphiadata.firebaseapp.com",
    "databaseURL": "https://delphiadata.firebaseio.com",
    "projectId": "delphiadata",
    "storageBucket": "delphiadata.appspot.com",
    "messagingSenderId": "319244349329",
    "appId": "1:319244349329:web:4aa5e609d50c8054d1f430",
    "measurementId": "G-W0FZZKMMS6"}
pyBase = pyrebase.initialize_app(configuracion)
db = pyBase.database()


data={
    'Clave':"123",
    'Correo':'j_e_salgado@ciencias.unam.mx',
    'Equipo':'B',
    'Estatus':'USUARIO',
    'Imagen':'Eduardo.png'
}
db.child('INTEGRANTES').child("Eduardo").set(data)

'''
