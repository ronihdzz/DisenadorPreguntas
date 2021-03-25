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

#Para poder usar esta clase primero debemos iniciar la comunicacion...
from CUERPO.LOGICA_creador.Creador_MisPaquetes import FuncionesCompresion



class StorageCuestionarios():
    def __init__(self,context,direccionJson):
        self.context = context
        self.direccionJson=direccionJson

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
            objetoStorageClient = storage.Client.from_service_account_json(self.direccionJson)
            self.controlStorageFirebase = FuncionesStorageFirebase(objetoStorageClient)
            return True
        except:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None

    def existeCuestionario(self, autorCuestionario, nombreCuestionario, mensajeActivado=True):
        listDictDatosCuestionarios=self.getDatosCuestionarios(autorCuestionario,mensajeActivado=False)
        listNombresCuestionarios=[x["NOMBRE"] for x in listDictDatosCuestionarios ]

        if listDictDatosCuestionarios!=None:#no ocurrio error al hacerlo...
            if nombreCuestionario in listNombresCuestionarios:
                return True
            else:
                return False
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()


    def puedoCompartirCuestionario(self,nombreUsuario,nombreCuestionarioCompartir,mensajeActivado=True):
        listDictDatosCuestionarios=self.getDatosCuestionarios(nombreUsuario)
        listNombresCuestionarios=[x["NOMBRE"] for x in listDictDatosCuestionarios ]

        if listDictDatosCuestionarios!=None:#no ocurrio error al hacerlo...
            if nombreCuestionarioCompartir in listNombresCuestionarios:
                if mensajeActivado:
                    QMessageBox.critical(self.context, "Atencion",
                                        "Ya has compartido un cuestionario\n"
                                        "con ese nombre,por lo que debes elegir\n"
                                        "otro nombre para este cuestionario\n"
                                        "que quieres compartir",
                                         QMessageBox.Ok)
                return False
            else:
                return True
        return None #error...


    def compartirUnTestDelphia(self,DictTestDelphia,mensajeActivado=True):
        operacionExitosa=False
        direcStorage=RecursosCreadorCuestionarios.DIREC_DELPHITEST_STORAGE
        destino=direcStorage+DictTestDelphia
        FuncionesCompresion.comprimirCarpeta(DictTestDelphia)#comprimimos la carpeta que copiamos a donde nos encontramos..
        #Subiendo el documento  al storage...
        resultado = self.controlStorageFirebase.subirDocumento(DictTestDelphia+".zip",destino+".zip")
        if resultado != None:
            operacionExitosa=True
        os.remove(DictTestDelphia + ".zip")  # borramos el archivo comprimido porque ya lo eliminamos...
        if operacionExitosa:
            if mensajeActivado:
                QMessageBox.critical(self.context, "Felicidades n.n",
                                     "El TEST_OFICIAL ha sido compartido\n"
                                     f"con exito rotundo.",
                                     QMessageBox.Ok)
            return True
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None

    def getPrefijoTestDelphia(self,mensajeActivado=True):
        operacionExitosa = False
        direcStorage = RecursosCreadorCuestionarios.DIREC_DELPHITEST_STORAGE
        listCuestionarios = self.controlStorageFirebase.getListNombresDocumentos(direcStorage)

        if listCuestionarios != None:  # NO HAY ERROR....
            punteroTest=len(listCuestionarios)+1
            prefijo="T"+str(punteroTest)+"_"
            operacionExitosa=True

        if operacionExitosa:
            if mensajeActivado:
                pass
            return prefijo
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None

    def ponerteAlCorriente_test(self,mensajeActivado):
        operacionExitosa = False
        direc = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES
        # obteniendo nombres de carpetas y archivos en esa ruta...
        a = os.listdir(direc)
        testUsuario_tiene=[]
        for x in a:
            nombre = direc + x
            if os.path.isdir(nombre):  # solo almacenando carpeta
                testUsuario_tiene.append(x)

        direcStorage = RecursosCreadorCuestionarios.DIREC_DELPHITEST_STORAGE
        testUsuario_debeTener = self.controlStorageFirebase.getListNombresDocumentos(direcStorage)
        if testUsuario_debeTener != None:  # NO HAY ERROR....
            #quitamos los .zip de los cuestionarios...
            testUsuario_debeTener=[x.replace(".zip","") for x in testUsuario_debeTener]
            #Convertimos las listas en conjuntos para hacer operaciones de ese indole...
            testUsuario_tiene=set(testUsuario_tiene)
            testUsuario_debeTener=set(testUsuario_debeTener)
            testUsuario_noTiene=testUsuario_debeTener-testUsuario_tiene
            testUsuario_noTiene=list(testUsuario_noTiene)
            testUsuario_noDebeTener=testUsuario_tiene-testUsuario_debeTener

            operacionExitosa=True
            for test in testUsuario_noDebeTener:
                # borramos TODOS los cuestionarios que el usuario ya no debe tener...
                shutil.rmtree(RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES+test)


            for test in testUsuario_noTiene:
                destinoTestDescargados=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES
                estado = self.controlStorageFirebase.descargarDocumento(direcStorage+test+".zip",
                                                                         test+".zip")
                if estado != None:  # se puedo descargar exitosamente...
                    # ahora descomprimimos el cuestionario en la misma carpeta...
                    FuncionesCompresion.descomprimirZip(test)
                    destinoTestDescargados += test #donde se descargara y que nombre tendra..

                    # Copiando TEST a la carpeta de los TEST_DELPHI...
                    shutil.copytree(test, destinoTestDescargados)
                    shutil.rmtree(test)  # borramos la carpeta que se paso en donde estamos..
                    os.remove(test + ".zip")  # borramos el .zip que se descargo en la carpeta...
                else:
                    operacionExitosa=False
                    break

        if operacionExitosa:
            if mensajeActivado:
                return True

        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
                return None

    def ponerteAlCorriente_compartidos(self,autor,mensajeActivado):
        operacionExitosa = False
        direc = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS
        # obteniendo nombres de carpetas y archivos en esa ruta...
        a = os.listdir(direc)
        testUsuario_tiene=[]
        for x in a:
            nombre = direc + x
            if os.path.isdir(nombre):  # solo almacenando carpeta
                testUsuario_tiene.append(x)#nombre del directorio...

        direcStorage=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
        direcStorage=direcStorage+autor+"/"

        #llavesCuestionarios = ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE","NOMBRE_FIREBASE")
        testUsuario_debeTener=self.getDatosCuestionarios(autor=autor,mensajeActivado=False)

        if testUsuario_debeTener != None:  # NO HAY ERROR....
            # lista de tuplas==> (NOMBRE_LOCAL /NOMBRE_FIREBASE)
            dictNombres={}
            for x in testUsuario_debeTener:
                dictNombres[x["NOMBRE"]] = x["NOMBRE_FIREBASE"]
            listNombreLocal=list(dictNombres.keys())

            #Convertimos las listas en conjuntos para hacer operaciones de ese indole...
            testUsuario_tiene=set(testUsuario_tiene)
            testUsuario_debeTener=set(listNombreLocal)
            testUsuario_noTiene=testUsuario_debeTener-testUsuario_tiene
            testUsuario_noTiene=list(testUsuario_noTiene)

            print("LLAVES.....",dictNombres)
            print("LLAVES.....",testUsuario_noTiene)

            operacionExitosa=True
            for test in testUsuario_noTiene:
                destinoTestDescargados=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS
                estado = self.controlStorageFirebase.descargarDocumento(direcStorage+dictNombres[test],
                                                                         test+".zip")
                if estado != None:  # se puedo descargar exitosamente...
                    # ahora descomprimimos el cuestionario en la misma carpeta...
                    # la funcion descomprimir le anexa el nombre de '.zip'
                    FuncionesCompresion.descomprimirZip(test)
                    destinoTestDescargados += test #donde se descargara y que nombre tendra..

                    # Copiando TEST a la carpeta de los TEST_DELPHI...
                    shutil.copytree(test, destinoTestDescargados)
                    shutil.rmtree(test)  # borramos la carpeta que se paso en donde estamos..
                    os.remove(test + ".zip")  # borramos el .zip que se descargo en la carpeta...
                else:
                    operacionExitosa=False
                    break

        if operacionExitosa:
            if mensajeActivado:
                return True

        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
                return None



    def compartirCuestionario(self,dictDatosCuestionarioCompartir,autor,documento,mensajeActivado=True):
        #llavesCuestionarios = ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")

        dataTime=dictDatosCuestionarioCompartir["DATA_TIME"]
        dataTime=dataTime.replace("/","X")
        dataTime = dataTime.replace(":", "x")
        dataTime = dataTime.replace(",", "H")

        claveCuestionario=self.getClaveCuestionario()

        dictDatosCuestionarioCompartir["DATA_TIME"]=dataTime
        dictDatosCuestionarioCompartir["CLAVE"]=claveCuestionario
        dictDatosCuestionarioCompartir["TERMINACION"]=".zip"

        ordenDatos=("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE","TERMINACION")

        #ordenamos los valores de las llaves del cuestionario...
        listValoresCuestinoario=[]
        for valor in ordenDatos:
            listValoresCuestinoario.append( str(dictDatosCuestionarioCompartir[valor])  )

        direcStorage = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
        print(listValoresCuestinoario)
        datosListos="_".join(listValoresCuestinoario) #separando cada dato con un "_" entre cada valor...
        destino=direcStorage+autor+'/'+datosListos
        print(datosListos)
        resultado=self.controlStorageFirebase.subirDocumento(documento,destino)
        if resultado!=None:
            if mensajeActivado:
                QMessageBox.critical(self.context, "Felicidades n.n",
                                     "Cuestionario compartido con exito\n"
                                     f"con clave de acceso: {claveCuestionario}",
                                     QMessageBox.Ok)
            return True
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None


    def getDatosCuestionarios(self,autor,mensajeActivado=True):

        direcStorage=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
        direcStorage=direcStorage+autor+"/"
        listCuestionarios=self.controlStorageFirebase.getListNombresDocumentos(direcStorage)

        if listCuestionarios!=None:#NO HAY ERROR....
            print("Cuestionarios:",listCuestionarios)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(listCuestionarios)

            llavesCuestionarios = ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE","NOMBRE_FIREBASE")

            listDictDatosCuestionarios=[]
            for datos in listCuestionarios:
                datosCuestionario=datos.split("_")[:-1] #excluimos el utlimo==>'.zip'
                                                        #[sdf,dfs,.zip]
                fecha=datosCuestionario[2]
                fecha=fecha.replace("X","/")
                fecha=fecha.replace("x",":")
                fecha=fecha.replace("H",",")
                datosCuestionario[2]=fecha #modificamos la fecha para que se pueda leer
                datosCuestionario.append(datos)#nombre real del cuestionario...
                listDictDatosCuestionarios.append( dict(zip(llavesCuestionarios,datosCuestionario )) )
            return listDictDatosCuestionarios
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None #eror de conexion...



    def eliminarCuestionario(self, autor, nombreCuestionarioEliminar,mensajeActivado=True):
        nombreRealCuestionario=self.getNombreReal(autor=autor,
                                                  nombreCuestionario=nombreCuestionarioEliminar,
                                                  mensajeActivado=False)

        if nombreRealCuestionario!=None: #si se encontro el nombre
            direcStorage = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
            direcStorage = direcStorage + autor + "/"

            nombreRealCuestionario = direcStorage + nombreRealCuestionario
            estado = self.controlStorageFirebase.borrarDocumento(nombreRealCuestionario)
            if estado != None:  # se puedo eliminar exitosamente
                if mensajeActivado:
                    QMessageBox.critical(self.context, "Felicidades n.n",
                                         "Cuestionario  eliminado\n"
                                         "exitosamente\n",
                                         QMessageBox.Ok)
                return True
            else:
                if mensajeActivado:
                    self.mensajeEmergenteError()
                return None
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None


    def descargarCuestionario(self,autor,nombreCuestionarioLocal,nombreCuestionarioStorage,mensajeActivado=True):
        direcStorage = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
        direcStorage = direcStorage + autor + "/"

        nombreRealCuestionario = direcStorage + nombreCuestionarioStorage
        #Le agregamos en '.zip' ya que asi se descarga inicialmente..
        estado = self.controlStorageFirebase.descargarDocumento(nombreRealCuestionario,nombreCuestionarioStorage)

        #quitamos el zip porque las funciones de comprension le agregan uno
        nombreCuestionarioStorage=nombreCuestionarioStorage.replace(".zip","")

        if estado != None:  # se puedo descargar exitosamente...
            #ahora descomprimimos el cuestionario en la misma carpeta...

            FuncionesCompresion.descomprimirZip(nombreCuestionarioStorage)

            destinoCuestinario = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS
            destinoCuestinario += nombreCuestionarioLocal
            # Copiando a la carpeta del cuestionarios compartidos...
            shutil.copytree(nombreCuestionarioLocal,destinoCuestinario)
            shutil.rmtree(nombreCuestionarioLocal)  # borramos la carpeta que se paso en donde estamos..
            os.remove(nombreCuestionarioStorage+".zip") #borramos el .zip que se descargo en la carpeta...
            QMessageBox.critical(self.context, "Felicidades n.n",
                                 "Cuestionario descargado\n"
                                 "exitosamente",
                                 QMessageBox.Ok)
            return True
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()


    def getNamesAllCreadores(self,mensajeActivado=True):
        direcStorage = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
        #Ponemos un prefix por que es el nombre de carpetas....
        listaCreadores = self.controlStorageFirebase.getListNombresDocumentos(direccionStorage=direcStorage,
                                                                              prefix='/')
        if listaCreadores!=None:
            listaCreadores=[x[:-1] for x in listaCreadores]
            return listaCreadores
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None #Error de internet...



    def getClaveCuestionario(self):
        # La función randint(a, b) genera un número entero entre a y b,
        # ambos incluidos. a debe ser inferior o igual a b.
        random.seed(datetime.now())
        claveCuestionario = random.randint(1000, 9999)  # generando de forma aleatoria un
        # numero de cuatro digitos
        return str(claveCuestionario)

    def getNombreReal(self,autor,nombreCuestionario,mensajeActivado=True):
        direcStorage = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
        direcStorage = direcStorage + autor + "/"
        listCuestionarios = self.controlStorageFirebase.getListNombresDocumentos(direcStorage)

        if listCuestionarios!=None: #no hay ningun error...
            # llavesCuestionarios = ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")
            indexNombreCuestionarioReal = -1
            for x in range(len(listCuestionarios)):
                datos=listCuestionarios[x]
                datosCuestionario = datos.split("_")[:-1]  # excluimos el utlimo==>'.zip'
                                                            # [sdf,dfs,.zip]
                if nombreCuestionario == datosCuestionario[0]:
                    indexNombreCuestionarioReal = x
                    break

            if indexNombreCuestionarioReal != -1:
                nombreRealCuestionario= listCuestionarios[indexNombreCuestionarioReal]
                return nombreRealCuestionario
            else:
                return None #no se encontro el cuestionario
        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None #no hay cuestionarios en la base de datos...



'''
    def descargarCuestionario(self,autor,nombreCuestionarioDescargar,mensajeActivado=True):
        nombreRealCuestionario=self.getNombreReal(autor=autor,
                                                  nombreCuestionario=nombreCuestionarioDescargar,
                                                  mensajeActivado=False)

        if nombreRealCuestionario!=None: #si se encontro el nombre
            direcStorage = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE
            direcStorage = direcStorage + autor + "/"

            nombreRealCuestionario = direcStorage + nombreRealCuestionario
            #Le agregamos en '.zip' ya que asi se descarga inicialmente..
            estado = self.controlStorageFirebase.descargarDocumento(nombreRealCuestionario,nombreCuestionarioDescargar+".zip")
            if estado != None:  # se puedo descargar exitosamente...
                #ahora descomprimimos el cuestionario en la misma carpeta...

                FuncionesCompresion.descomprimirZip(nombreCuestionarioDescargar)

                destinoCuestinario = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS
                destinoCuestinario += nombreCuestionarioDescargar
                # Copiando a la carpeta del cuestionarios compartidos...
                shutil.copytree(nombreCuestionarioDescargar,destinoCuestinario)
                shutil.rmtree(nombreCuestionarioDescargar)  # borramos la carpeta que se paso en donde estamos..
                os.remove(nombreCuestionarioDescargar+".zip") #borramos el .zip que se descargo en la carpeta...
                QMessageBox.critical(self.context, "Felicidades n.n",
                                     "Cuestionario descargado\n"
                                     "exitosamente",
                                     QMessageBox.Ok)
                return True
            else:
                if mensajeActivado:
                    self.mensajeEmergenteError()

        else:
            if mensajeActivado:
                self.mensajeEmergenteError()
            return None
'''