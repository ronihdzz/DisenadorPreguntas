from PyQt5 import QtWidgets,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal,QObject
from PyQt5.QtWidgets import  QMessageBox
from datetime import datetime
import shutil, os
import os
import random
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Main.CreadorPreguntasMain_d import Ui_MainWindow
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.menuTipoPreguntas import menuTipoPreguntas
from CUERPO.LOGICA_creador.Creador_Pregunta_Binaria.PreguntaBinaria import PreguntaBinaria
from CUERPO.LOGICA_creador.Creador_Pregunta_Multiple.PreguntaMultiple import PreguntaMultiple
from CUERPO.LOGICA_creador.Creador_Preguna_CheckBox.PreguntaCheckBox import PreguntaCheckBox
from CUERPO.LOGICA_creador.Creador_Pregunta_Abierta.PreguntaAbierta import PreguntaAbierta
from CUERPO.LOGICA_creador.Creador_Main.CreadorPreguntasVacio import CreadorPreguntasVacio

from CUERPO.LOGICA_creador.Creador_Ejecutador.Visualizador import VisualizadorPreguntas
from CUERPO.LOGICA_creador.Creador_Ejecutador.CreadorCuestionarios import EjecutadorCuestionario
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.EditorNombreArchivo import EditarNombre
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.PanelCuestionariosMain import PanelCuestionariosMain

from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.ConfirmadorAccion import ConfirmadorAccion
###############################################################
#  MIS LIBRERIAS...
##############################################################
#Importando la clase que uso para la base de datos sqlite...
from CUERPO.LOGICA_creador.Creador_MisPaquetes.DataBaseCreadorPreguntas import DataBaseCreadorPreguntas
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios

class CreadorPreguntas(QtWidgets.QMainWindow, Ui_MainWindow):
    senalTermino = pyqtSignal(bool)  # comunicacion con la aplicacion
    senalCuestionarioCompartido=pyqtSignal(bool)
    senalTestCompartido=pyqtSignal(bool)

    def __init__(self,nombreCreador="ANONIMO",nombreCuestionario="",listNombresExistentes=[]):
        Ui_MainWindow.__init__(self)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.extensionCuestionario=RecursosCreadorCuestionarios.TERMINACION_CUESTIONARIOS
        self.listNombresExistentes=listNombresExistentes
        if nombreCuestionario=="":
            nombreCuestionario=nombreCreador+"_"+self.getNameDefault()

        self.nombreCuestionario = nombreCuestionario
        self.setWindowTitle(f"Nombre de cuestionario: {nombreCuestionario}")
        self.nombreCarpeta=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION+nombreCuestionario
        self.nombreCreador=nombreCreador
        self.abrirCuestionario()

        self.listBotonesPreguntas=[]
        self.listIdPreguntas=[]

        self.punteroPregunta=-1 #numero que no puede ser ningun puntero al incio

        #Acciones del menu...
        self.actionCrear_nueva_pregunta.setShortcut("Ctrl+p")
        self.actionVisualizar.setShortcut("F5")
        self.actionCambiar_nombre.setShortcut("Ctrl+n")
        self.actionEjecutar_cuestionario.setShortcut("F9")


        self.actionCrear_nueva_pregunta.triggered.connect(self.abrirMenuPreguntas)
        self.actionEjecutar_cuestionario.triggered.connect(self.ejecutarCuestionario)
        self.actionVisualizar.triggered.connect(self.compilarPregunta)
        self.actionImportar_otro_cuestionario_2.triggered.connect(self.mostrarMisCuestionarios)
        self.actionEliminar_todo_el_cuestionario.triggered.connect(self.mensajeAlerta_eliminarTodoCuestinoario)
        #self.actionCompartir_cuestionario_al_servidor.triggered.connect(self.mensajeAlerta_compartirCuestionario)
        #self.actionSubir_cuestionario_cuestionario_como_cuestionario_final.triggered.connect(self.mensajeAlerta_compartirTest)


        self.actionCambiar_nombre.triggered.connect(self.editarNombre)


        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll_barra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setWidget(self.widget)



        self.btn_mas.clicked.connect(self.abrirMenuPreguntas)

        #creando multiples ventanas...
        self.ventanas=[]
        self.ventanas.append( PreguntaBinaria(self.nombreCreador,self.nombreCarpetaImagenes)  )#pregunta binaria
        self.ventanas.append( PreguntaMultiple(self.nombreCreador,self.nombreCarpetaImagenes)  ) #pregunta multiple
        self.ventanas.append( PreguntaCheckBox(self.nombreCreador,self.nombreCarpetaImagenes)  ) #pregunta checbox
        self.ventanas.append( PreguntaAbierta(self.nombreCreador,self.nombreCarpetaImagenes) )#pregunta abierta
        self.ventanas.append( CreadorPreguntasVacio() )  # pregunta abierta

        #Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelPreguntas.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelPreguntas.setCurrentIndex(4) #WIDGET VACIO....
        self.listWidget_panelPreguntas.showFullScreen()

        self.listBotonesPreguntas=[]
        self.contadorPreguntas=0

        self.IMAGEN_ELIMINAR=RecursosCreadorCuestionarios.ICONO_TACHE
        self.IMAGEN_ELIMINAR_2=RecursosCreadorCuestionarios.ICONO_TACHE_2

        self.controlABSOLUTO_visualizador=VisualizadorPreguntas(direc_carpetaImagenes=self.nombreCarpetaImagenes)
        self.controlABSOULUTO_editorNombre=EditarNombre(self.listNombresExistentes)
        self.controlABSOULUTO_editorNombre.senalNombreElegido.connect(self.usuarioCambioNombre)


        self.listIdPreguntas = list(self.controlABSOLUTO_baseDatos.getAllIds_preguntas())
        if len(self.listIdPreguntas)>0:
            self.abrirPreguntasPrevias()

        self.crearArchivoDatos()
        self.CUESTIONARIO_FUE_ELIMINADO = False

        self.NUEVO_NOMBRE=None


    def editarNombre(self):
        self.controlABSOULUTO_editorNombre.show()

    def usuarioCambioNombre(self,nuevoNombre):
        self.setWindowTitle(f"Nombre de cuestionario: {nuevoNombre}")
        self.NUEVO_NOMBRE=nuevoNombre

        '''
        def mensajeAlerta_compartirCuestionario(self):
            # Obtener la lista de cuestionarios compartidos...
            cuestionarioCompartir=self.nombreCuestionario
            if self.NUEVO_NOMBRE!=self.nombreCuestionario and self.NUEVO_NOMBRE!=None:
                cuestionarioCompartir=self.NUEVO_NOMBRE
    
            controlABSOLUTO_storageCuestionarios = StorageCuestionarios(self,
                                                                        RecursosCreadorCuestionarios.DIRE_JSON)
            # iniciamos comunicacion con el servidor
            comunicacion =controlABSOLUTO_storageCuestionarios.iniciarComunicacion(mensajeActivado=True)
            if comunicacion:  # si la primera comunicacion fue exitosa..
                puedoCompartir=controlABSOLUTO_storageCuestionarios.puedoCompartirCuestionario(nombreUsuario=self.nombreCreador,
                                                                                       nombreCuestionarioCompartir=cuestionarioCompartir,
                                                                                       mensajeActivado=True)
                if puedoCompartir!=None: #sin errores...
                    if puedoCompartir:#el cuestionario que quiero compartir existe...
                        indicaciones="Debes de estar consciente que SOLO se recomienda COMPARTIR "
                        indicaciones+="cuestionarios cuando ya terminaste tu parte del trabajo  "
                        indicaciones+="y quieres que algun miembro del equipo  lo pueda descargar "
                        indicaciones+="para posteriormente unirlo con su cuestionario.No se "
                        indicaciones+="recomienda estar compartiendo constantemente cuestionarios "
                        indicaciones+="en la base de datos de delphia, ya que genera  gastos de recursos "
                        indicaciones+="pero si es necesario puedes hacerlo n.n.\n"
                        indicaciones+="En funcion de lo explicado anteriormente, si sigues con la intencion "
                        indicaciones+="de compartir tu cuestionario porfavor acompleta la frase."
                        clave="compartir cuestionario"
                        self.confirmadorAccion=ConfirmadorAccion(indicaciones=indicaciones,
                                                                 palabraConfirmacion=clave)
                        self.confirmadorAccion.accionConfirmada.connect(self.compartirCuestionario)
                        self.confirmadorAccion.show()
    
    
        def mensajeAlerta_compartirTest(self):
            if self.contadorPreguntas<5:
                QMessageBox.question(self, "Delphi",
                                     "Para subir un TestOficial,este debe\n"
                                     "tener,almenos 15 preguntas",
                                      QMessageBox.Ok)
            else:
    
                indicaciones="Debes de estar consciente que SOLO se recomienda SUBIR TEST "
                indicaciones+="SI Y SOLO SI, estas seguro que todo su contenido es correcto,"
                indicaciones+="ya que al subirlo, este se adjuntara en LA CARPETA OFICIAL DE "
                indicaciones+="TEST_DELHPIA, y el proceso para poder borrarlo en caso de presentar errores "
                indicaciones+="es sumamente complejo, y no podras tu  realizar  dicho proceso, si no "
                indicaciones+="unicamente los PROGRAMADORES DE LA BASE DE DATOS DE DELPHIA, asi que SOLO "
                indicaciones+="SE RECOMIENDA SUBIR EL CUESTIONARIO, SI Y SOLO SI, estas totalmente seguro "
                indicaciones+="QUE TODAS LAS PREGUNTAS ESTAN FORMULADAS CORRECTAMENTE ASI COMO SUS ACIERTOS.\n"
                indicaciones+="Es importante recordarte que al subir este cuestionario, este cuestionario se borrara  "
                indicaciones+="de tu carpeta de CUESTIONARIOS EN EDICION, ya que consideramos que ya no es necesario "
                indicaciones+="que lo tengas, pues  ya lo has compartido como TEST OFICIAL, lo cual significa que ya no "
                indicaciones+="hay mas modificaciones que hacerle,sin embargo,si por alguna extraña razon, lo quisieras "
                indicaciones+="recuperar, podras descargarlo en el apartado de TEST_DELPHIA.\n"
                indicaciones+="En funcion de lo explicado anteriormente, si sigues con la intencion "
                indicaciones+="de de SUBIR ESTE TEST, por favor acompleta la frase."
                clave="Subir Test Oficial"
                self.confirmadorAccion=ConfirmadorAccion(indicaciones=indicaciones,
                                                         palabraConfirmacion=clave)
                self.confirmadorAccion.accionConfirmada.connect(self.compartirTest)
                self.confirmadorAccion.show()
    
    
        def compartirTest(self):
            controlABSOLUTO_storageCuestionarios = StorageCuestionarios(self,
                                                                        RecursosCreadorCuestionarios.DIRE_JSON)
            # iniciamos comunicacion con el servidor
            comunicacion = controlABSOLUTO_storageCuestionarios.iniciarComunicacion(mensajeActivado=True)
            if comunicacion:  # si la primera comunicacion fue exitosa..
                prefijoNombreTest = controlABSOLUTO_storageCuestionarios.getPrefijoTestDelphia(mensajeActivado=True)
                if prefijoNombreTest != None:  # el prefijo del cuestionario se obtuvo con exito...
                    nombreCuestionario = self.nombreCuestionario #obteniendo el nombre del cuestionario
                    #nombre donde se ubica nuestro cuestionario...
                    nombreCarpeta = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION + nombreCuestionario + "/"
                    # Copiando la carpeta del cuestionario a donde nos encontramos con el nombre del cuestionario...
                    shutil.copytree(nombreCarpeta, nombreCuestionario)
                    nombreCuestionario_nuevo = self.NUEVO_NOMBRE
    
                    if nombreCuestionario_nuevo != None and nombreCuestionario != nombreCuestionario_nuevo:
                        #agregando el prefijo al cuestionario test que se subira...
                        nombreCuestionario_nuevo=prefijoNombreTest+nombreCuestionario_nuevo
                    else:
                        nombreCuestionario_nuevo=prefijoNombreTest+nombreCuestionario
    
                    nombreCarpeta_PREV = nombreCuestionario + "/"  # no le ponemos ruta porque nos encontramos en esta carpeta...
                    nombreBaseDatos_PREV = nombreCarpeta_PREV + nombreCuestionario + ".db"
                    nombreCarpetaImagenes_PREV = nombreCarpeta_PREV + RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES + nombreCuestionario + "/"
                    nombreArchivoDatos_PREV = nombreCarpeta_PREV + nombreCuestionario + ".txt"
    
                    nombreBaseDatos_NEW = nombreCarpeta_PREV + nombreCuestionario_nuevo + ".db"
                    nombreCarpetaImagenes_NEW = nombreCarpeta_PREV + RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES + nombreCuestionario_nuevo + "/"
                    nombreArchivoDatos_NEW = nombreCarpeta_PREV + nombreCuestionario_nuevo + ".txt"
    
                    nombreCarpeta_NEW = nombreCuestionario_nuevo + "/"
    
                    # Cambiando nombres...
                    os.rename(nombreArchivoDatos_PREV, nombreArchivoDatos_NEW)
                    os.rename(nombreBaseDatos_PREV, nombreBaseDatos_NEW)
                    os.rename(nombreCarpetaImagenes_PREV, nombreCarpetaImagenes_NEW)
                    os.rename(nombreCarpeta_PREV, nombreCarpeta_NEW)
    
                    nombreCarpetaComprimira = nombreCuestionario_nuevo
    
                   #compartiendo cuestionario...
                    operacionExitosa = controlABSOLUTO_storageCuestionarios.compartirUnTestDelphia(
                            DictTestDelphia=nombreCarpetaComprimira,
                            mensajeActivado=True)
                    if operacionExitosa != None:  # el cuestionario se compartio con exito..
                        #copiando carpeta a la seccion de cuestionarios test...
                        shutil.copytree(nombreCarpetaComprimira,
                                        RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES+nombreCarpetaComprimira)
                        shutil.rmtree(nombreCarpetaComprimira)
                        # self.usuarioCambioNombre(nombreCarpetaComprimira) #el nombre del archivo del test..
                        self.senalTestCompartido.emit(True)
                        self.eliminarTodoCuestionario()
                    else:
                        shutil.rmtree(nombreCarpetaComprimira)
                        #self.close()  # cerramos el cuestionario y lo abriremos en los cuestionarios compartidos...
                    # borramos la carpeta que se compartio CON o SIN EXITO...
    
        def compartirCuestionario(self):
    
            nombreCuestionario = self.nombreCuestionario
            nombreCarpeta = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION + nombreCuestionario + "/"
    
            #Copiando la carpeta del cuestionario a donde nos encontramos con el nombre del cuestionario...
            shutil.copytree(nombreCarpeta, nombreCuestionario)
    
            nombreCarpetaComprimira = nombreCuestionario
            nombreCuestionario_nuevo=self.NUEVO_NOMBRE
    
            if nombreCuestionario_nuevo != None and nombreCuestionario != nombreCuestionario_nuevo:
                nombreCarpeta_PREV = nombreCuestionario + "/"  # no le ponemos ruta porque nos encontramos en esta carpeta...
                nombreBaseDatos_PREV = nombreCarpeta_PREV + nombreCuestionario + ".db"
                nombreCarpetaImagenes_PREV = nombreCarpeta_PREV + RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES + nombreCuestionario + "/"
                nombreArchivoDatos_PREV = nombreCarpeta_PREV + nombreCuestionario + ".txt"
    
                nombreBaseDatos_NEW = nombreCarpeta_PREV + nombreCuestionario_nuevo + ".db"
                nombreCarpetaImagenes_NEW = nombreCarpeta_PREV + RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES + nombreCuestionario_nuevo + "/"
                nombreArchivoDatos_NEW = nombreCarpeta_PREV + nombreCuestionario_nuevo + ".txt"
    
                nombreCarpeta_NEW = nombreCuestionario_nuevo + "/"
    
                # Cambiando nombres...
                os.rename(nombreArchivoDatos_PREV, nombreArchivoDatos_NEW)
                os.rename(nombreBaseDatos_PREV, nombreBaseDatos_NEW)
                os.rename(nombreCarpetaImagenes_PREV, nombreCarpetaImagenes_NEW)
                os.rename(nombreCarpeta_PREV, nombreCarpeta_NEW)
    
                nombreCarpetaComprimira = nombreCuestionario_nuevo
    
            # Copiando la carpeta del cuestionarios compartidos...
            shutil.copytree(nombreCarpetaComprimira,RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS+nombreCarpetaComprimira)
            FuncionesCompresion.comprimirCarpeta(nombreCarpetaComprimira)  # comprimimos la carpeta que copiamos a donde nos encontramos..
            shutil.rmtree(nombreCarpetaComprimira)  # borramos la carpeta que se paso en donde estamos...
    
            #ordenDatos=("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE","TERMINACION")
            #datos del cuestionario...
            data={}
            data["NOMBRE"]=nombreCarpetaComprimira #nombre del cuestionario compartira
            data["ORDEN"]=self.getNameDefault() #nos dara el tiempo en segundos con 4 numeros decimales
            data["DATA_TIME"]=self.getFecha()
            data["PREGUNTAS"]=self.contadorPreguntas #numero de preguntas
    
    
            controlABSOLUTO_storageCuestionarios = StorageCuestionarios(self,
                                                                        RecursosCreadorCuestionarios.DIRE_JSON)
            # iniciamos comunicacion con el servidor
            comunicacion =controlABSOLUTO_storageCuestionarios.iniciarComunicacion(mensajeActivado=True)
            if comunicacion:  # si la primera comunicacion fue exitosa..
                estado=controlABSOLUTO_storageCuestionarios.compartirCuestionario(dictDatosCuestionarioCompartir=data,
                                                                           autor=self.nombreCreador,
                                                                           documento=nombreCarpetaComprimira+".zip",
                                                                           mensajeActivado=True)
                if estado!=None: #el cuestionario se compartio con exito..
                    self.senalCuestionarioCompartido.emit(True)
                    self.close() #cerramos el cuestionario y lo abriremos en los cuestionarios compartidos...
            os.remove(nombreCarpetaComprimira + ".zip")  # borramos la carpeta que comprimimos
        '''

    def mensajeAlerta_eliminarTodoCuestinoario(self):
        indicaciones="Debes de estar consciente que al eliminar "
        indicaciones+="el cuestionario,lo haras de forma permanente,por lo cual "
        indicaciones+="NO habra forma de recuperarlo, almenos que lo hayas "
        indicaciones+="compartido  en DelphiData. ¿En realidad quieres eliminar "
        indicaciones+="todo el cuestionario?"

        clave="Eliminar todo el cuestionario"

        self.confirmadorAccion=ConfirmadorAccion(indicaciones=indicaciones,
                                                 palabraConfirmacion=clave)
        self.confirmadorAccion.accionConfirmada.connect(self.eliminarTodoCuestionario)
        self.confirmadorAccion.show()

    def eliminarTodoCuestionario(self):
        shutil.rmtree(self.nombreCarpeta)
        self.CUESTIONARIO_FUE_ELIMINADO=True
        self.close()


    def mostrarMisCuestionarios(self):
        self.panelMisCuestionarios=PanelCuestionariosMain()
        self.panelMisCuestionarios.senalCuestionarioElegido.connect(self.importarCuestionario)
        #la senal dara un dicionario con los siguientes datoos...
        # dictInfo==> llaves:NOMBRE y TIPO==>DESCARGADOS OR MIOS
        self.panelMisCuestionarios.show()

    #numberQuestionRandom=None  si tiene un valor diferente de None...
    #significa que importara x de forma aleatoria del cuestionario a importar
    #si 'numberQuestionRandom' es MAYOR al numero de preguntas del cuestionario
    #a importar, importara todo el cuestionario...
    def importarCuestionario(self,dictInfo,numberQuestionRandom=None):
        # dictInfo==> llaves:NOMBRE y TIPO==>DESCARGADOS OR MIOS OR OFICIALES

        nombreCuestionarioImportar=dictInfo["NOMBRE"]
        if dictInfo["TIPO"]=="MIOS": #SE QUIERE IMPORTAR CUESTIONARIOS DE LOS MIOS...
            nombreCarpeta=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION+nombreCuestionarioImportar+"/"

        elif dictInfo["TIPO"]=="DESCARGADOS": #SE QUIERE IMPORTAR CUESTIONARIOS DE LA CARPETA DE DESCARGAS...
            nombreCarpeta=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS+nombreCuestionarioImportar+"/"

        else: #oficiales...
            nombreCarpeta = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES+nombreCuestionarioImportar+"/"


        nombreBaseDatos=nombreCarpeta+nombreCuestionarioImportar
        nombreCarpetaImagenes=nombreCarpeta+RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES+nombreCuestionarioImportar+"/"


        #Copiando las imagenes de un directorio al otro...
        destino=self.nombreCarpetaImagenes #la carpeta de imagenes en donde pegaremos
        origen=nombreCarpetaImagenes #la carpeta de imagenes que copearemos..

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if os.path.exists(origen):
            listaArchivos = os.listdir(origen)
            for x in listaArchivos:
                print(x)
                if '.' in x:  # los nombres de las imagenes tienen puntos...
                    archivoCopeara = origen + x
                    lugarDondeGuardara = destino + x
                    shutil.copy(archivoCopeara, lugarDondeGuardara)

        #Ya que copeamos la carpeta de imagenes ahora sigue el contenido de la base de datos...
        controlBASE_DATOS=DataBaseCreadorPreguntas(nombreBaseDatos)

        #obteniendo una lista de todos los ids de las preguntas de la base de datos que deseamos importar..
        listaIDs=controlBASE_DATOS.getAllIds_preguntas()
        # osea significa que quieren importar un cuestionario de forma aleatoria...
        if numberQuestionRandom!=None:
            #si el numero de muestra a tomar es menor,usamos la funcion que...
            #selecciona al azar más de un elemento de la lista sin elementos repetidos
            if numberQuestionRandom<len(listaIDs):
                listaIDs=random.sample(listaIDs,numberQuestionRandom)
        listaIDs_asignadosPorEstaBase=[]

        for id in listaIDs:
            datosPregunta,datosRespuesta=controlBASE_DATOS.getData(id)
            print(datosPregunta)
            print(datosRespuesta)
            print("*****************************************************")
            tipoRespuesta = datosPregunta["TIPO_RESPUESTA"]  # AHI SE ENCUENTRA EL TIPO DE RESPUESTA...
            # Eliminamos datos que no necesita...
            del datosPregunta["TIPO_RESPUESTA"]
            del datosPregunta["ID"]

            datosPregunta_tupla=tuple(datosPregunta.values())
            datosRespuesta_tupla=None
            if tipoRespuesta != 3:  # pues las preguntas imagenes no tienen dataRespuesta
                del datosRespuesta["ID"]
                datosRespuesta_tupla=tuple(datosRespuesta.values() )

            #agregan los datos a la otra base de datos..
            newId=self.controlABSOLUTO_baseDatos.addNewQuestion(tipoRespuesta,datosPregunta_tupla,datosRespuesta_tupla)
            print("NUEVO ID:...",newId)
            listaIDs_asignadosPorEstaBase.append(newId)
            print(datosPregunta_tupla)
            print(datosRespuesta_tupla)

        #despues de fusionar el contenido de ambas bases de datos, podemos proseguir a
        #mostrar las nuevas preguntas importadas...
        #Abriendo preguntas antiguas de existir....
        #concatenando ambas lista de ids...

        print("LISTA IDS ASIGNADOS..",listaIDs_asignadosPorEstaBase)
        self.listIdPreguntas+=listaIDs_asignadosPorEstaBase

        #guardamos el ultimo puntero ya que fue al agregar preguntas
        #este cambiara de valor
        PUNTERO_ID_ANTES_JUNTAR_PREGUNTAS = self.punteroPregunta
        self.guardarCambios() #guardamos antes de agregar las preguntas y cambiar de puntero...

        for x in listaIDs_asignadosPorEstaBase:
            self.agregarBotonPreguntaAlPanel()

        # El ultimo contenido de la pregunta debe ser cargado...
        self.verContenidoPregunta(self.punteroPregunta)


    def abrirPreguntasPrevias(self):
        #Abriendo preguntas antiguas de existir....
        for x in self.listIdPreguntas:
            self.agregarBotonPreguntaAlPanel()

        #El ultimo contenido de la pregunta debe ser cargado...
        self.verContenidoPregunta(self.punteroPregunta)


    def abrirCuestionario(self):
        #Si la carpeta del cuestinario NO existe pues hay que crearla
        if not( os.path.exists(self.nombreCarpeta) ):
            os.mkdir(self.nombreCarpeta)
        #Vamos si existe la carpeta de imagenes...
        self.nombreCarpetaImagenes=self.nombreCarpeta+"/"+RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES+self.nombreCuestionario+"/"
        if not( os.path.exists(self.nombreCarpetaImagenes) ):
            os.mkdir(self.nombreCarpetaImagenes)

        self.controlABSOLUTO_baseDatos = DataBaseCreadorPreguntas(self.nombreCarpeta+"/"+self.nombreCuestionario)
        self.controlABSOLUTO_baseDatos.crearBaseDatos()


    def crearArchivoDatos(self):
        nombreJSON_datos=self.nombreCarpeta+"/"+self.nombreCuestionario+".txt"

        data={}
        data["ORDEN"]=self.getNameDefault() #nos dara el tiempo en segundos con 4 numeros decimales
        data["DATA_TIME"]=self.getFecha()
        data["PREGUNTAS"]=self.contadorPreguntas #numero de preguntas

        # eliminar el ultimo boton del panel....
        # import ast
        # configuracion=ast.literal_eval(data)#convirtiendo texto a un diccionario
        with open(nombreJSON_datos,"w") as file:
            file.write(str(data))



    def closeEvent(self, event):
        if not(self.CUESTIONARIO_FUE_ELIMINADO):
            self.crearArchivoDatos()
            if self.NUEVO_NOMBRE!=None and self.NUEVO_NOMBRE!=self.nombreCuestionario:
                #Significa que cambio de nombre

                nombreCarpeta_PREV = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION + self.nombreCuestionario + "/"
                nombreBaseDatos_PREV = nombreCarpeta_PREV+ self.nombreCuestionario + ".db"
                nombreCarpetaImagenes_PREV = nombreCarpeta_PREV + RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES + self.nombreCuestionario + "/"
                nombreArchivoDatos_PREV = nombreCarpeta_PREV + self.nombreCuestionario + ".txt"

                nombreBaseDatos_NEW = nombreCarpeta_PREV + self.NUEVO_NOMBRE+".db"
                nombreCarpetaImagenes_NEW = nombreCarpeta_PREV + RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES + self.NUEVO_NOMBRE + "/"
                nombreArchivoDatos_NEW=nombreCarpeta_PREV + self.NUEVO_NOMBRE+".txt"

                nombreCarpeta_NEW = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION + self.NUEVO_NOMBRE + "/"

                #Cambiando nombres...
                os.rename(nombreArchivoDatos_PREV,nombreArchivoDatos_NEW)
                os.rename(nombreBaseDatos_PREV,nombreBaseDatos_NEW)
                os.rename(nombreCarpetaImagenes_PREV,nombreCarpetaImagenes_NEW)
                os.rename(nombreCarpeta_PREV,nombreCarpeta_NEW)

        self.senalTermino.emit(True)


    def ejecutarCuestionario(self):
        if self.contadorPreguntas>0:
            self.guardarCambios() #antes de ejecutar el cuestinario debemos guardar los cambios...
            self.ejecutadorCuestionario= EjecutadorCuestionario(nombreCuestionario=self.nombreCuestionario,mios=True)
            self.ejecutadorCuestionario.show()



    def compilarPregunta(self):
        self.statusbar.showMessage('Compilando pregunta...', 1000)

        widgetPregunta = self.listWidget_panelPreguntas.currentIndex()  # nos dira en que pregunta nos econtramos...

        #self.ventanas[widgetPregunta].listWidget_panelVersion.currentIndex() #nos dira el tipo de respuesta...

        datosPregunta, datosRespueta = self.ventanas[widgetPregunta].getDatos(False)

        self.controlABSOLUTO_visualizador.visualizarPregunta(widgetPregunta,datosPregunta,datosRespueta)
        self.controlABSOLUTO_visualizador.show()


    def guardarCambios(self):
        if self.contadorPreguntas>0:
            print("GUARADAR...")
            #mostrando mensaje por 1 segundo

            #Nos dira en que tipo de pregunta nos encontramos....
            widgetPregunta=self.listWidget_panelPreguntas.currentIndex() #nos dira en que pregunta nos econtramos...
            #Esa pregunta nos dira que datos son los que ella tiene...
            datosPregunta,datosRespueta=self.ventanas[widgetPregunta].getDatos()
            print("Datos a guardar...",datosPregunta,datosRespueta)
            #En funcion de en que numero de pregunta nos encontramos retornamos el ID real...
            #para despues poder actualizar sus n
            idPregunta=self.listIdPreguntas[self.punteroPregunta]
            self.controlABSOLUTO_baseDatos.actualizarDatosPregunta(idPregunta,datosPregunta,datosRespueta)
            self.statusbar.showMessage('Guardando cambios...',1000)


    def abrirMenuPreguntas(self):
        #mostrando mensaje por 1 segundo
        self.statusbar.showMessage('Creando nueva pregunta...',1000)
        self.ventanaMenuPregunta=menuTipoPreguntas()
        self.ventanaMenuPregunta.usuarioEscogioPregunta.connect(self.crearNuevaPregunta)
        self.ventanaMenuPregunta.show()

    def crearNuevaPregunta(self, tipoRespuesta):
           # guardar cambios de la anterior pregunta antes de pasar a la siguinte
            self.guardarCambios()
            datosPregunta,datosRespuesta=self.ventanas[tipoRespuesta].preguntaBlanco()
            idNewPregunta=self.controlABSOLUTO_baseDatos.addNewQuestion(tipoRespuesta,datosPregunta,datosRespuesta)
            if idNewPregunta==False:#Si hay un error al crear la pregunta...
                pass
            else:
                self.listWidget_panelPreguntas.setCurrentIndex(tipoRespuesta)
                self.listIdPreguntas.append(idNewPregunta)#agregando el id de la pregunta...
                self.agregarBotonPreguntaAlPanel()


    def agregarBotonPreguntaAlPanel(self):
        widget = QWidget()
        widget.setMinimumSize(60,75)
        widget.setMaximumSize(60,75)
        gridLayout = QGridLayout(widget)  # Set the checkbox in the layer
        botonCerrar = QPushButton()
        a = "QPushButton{border-image:url(" + self.IMAGEN_ELIMINAR + ");}"
        b = "QPushButton:hover{border-image:url(" + self.IMAGEN_ELIMINAR_2 + ");}"
        c = "QPushButton:pressed{border-image:url(" + self.IMAGEN_ELIMINAR + ");}"
        botonCerrar.setStyleSheet(a + b + c)
        botonCerrar.setMaximumSize(15,15)
        botonCerrar.setMinimumSize(15,15)
        botonPregunta=QPushButton()
        botonPregunta.setMaximumSize(50,50)
        botonPregunta.setMinimumSize(50,50)
        nuevoBotonPregunta=BotonPregunta(self.contadorPreguntas,botonPregunta,botonCerrar)

        self.listBotonesPreguntas.append(nuevoBotonPregunta)
        nuevoBotonPregunta.clickBotonPregunta.connect(self.guardarYverContenidoPregunta)
        nuevoBotonPregunta.suHoraMorir.connect(self.eliminarPregunta)
        #nuevoBotonPregunta.darIdBotonPregunta()  # hacer como que lo selecciona...


        # addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        gridLayout.addWidget(botonCerrar, 0, 0, 1, -1, alignment=QtCore.Qt.AlignRight)
        gridLayout.addWidget(botonPregunta,1, 0, -1, -1,alignment=QtCore.Qt.AlignHCenter)
        gridLayout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding


        #Desmarcamos el boton antiguo,y marcamos el siguiente
        self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(False)
        self.punteroPregunta = self.contadorPreguntas
        self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(True)
        self.vbox.addWidget(widget, alignment=QtCore.Qt.AlignHCenter)

        self.contadorPreguntas += 1


    def verContenidoPregunta(self,idBoton):
            self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(False)
            self.punteroPregunta=idBoton
            self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(True)

            idPregunta = self.listIdPreguntas[idBoton]
            dataPregunta,dataRespuesta=self.controlABSOLUTO_baseDatos.getData(idPregunta)
            print("ABRIENDO DATOS DE LA PREGUNTA....")
            print(dataPregunta,dataRespuesta)

            #widgetPregunta = self.listWidget_panelPreguntas.currentIndex()  # nos dira en que pregunta nos econtramos...
            tipoRespuesta=dataPregunta["TIPO_RESPUESTA"] #AHI SE ENCUENTRA EL TIPO DE RESPUESTA...
            self.listWidget_panelPreguntas.setCurrentIndex(tipoRespuesta)
            self.ventanas[tipoRespuesta].preguntaBlanco()
            #Eliminamos datos que no necesita...
            del dataPregunta["TIPO_RESPUESTA"]
            del dataPregunta["ID"]
            if tipoRespuesta!=3: #pues las preguntas imagenes no tienen dataRespuesta
                del dataRespuesta["ID"]
            self.ventanas[tipoRespuesta].abrirPregunta(dataPregunta,dataRespuesta)

    def guardarYverContenidoPregunta(self, idBoton):
        if self.punteroPregunta!=idBoton:
            self.guardarCambios()#guardando los cambios de la pregunta antes de pasar a la otra...
            self.verContenidoPregunta(idBoton)



    def eliminarPregunta(self, posItemMatar):
        self.guardarYverContenidoPregunta(posItemMatar)
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quieres\n"
                                         f"eliminar la pregunta numero: {posItemMatar + 1}?",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            pass
            idPreguntaEliminar=self.listIdPreguntas[posItemMatar]#eliminar el id de ahi....

            layout = self.vbox
            noWidgetBorrar = self.contadorPreguntas-1 #ya que la posicion inicia desde cero
            widgetToRemove = layout.itemAt(noWidgetBorrar).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)
            self.controlABSOLUTO_baseDatos.eliminarPregunta(idPreguntaEliminar) #eliminar el id de la base de datos...
            self.listBotonesPreguntas.pop() #eliminar el ultimo objeto
            self.listIdPreguntas.pop(posItemMatar)
            self.contadorPreguntas-=1 #actualizamos el numero de preguntas

            #si la pregunta eliminada no fue la ultima sobrante y aparte no fue
            #la ultima pregunta creada, entonces...
            if self.contadorPreguntas>0 and self.punteroPregunta!=self.contadorPreguntas:
                self.verContenidoPregunta(self.punteroPregunta)
            #si la pregunta eliminada fue la ultima preguna...
            elif self.punteroPregunta==self.contadorPreguntas and self.punteroPregunta!=0:
                self.punteroPregunta=self.punteroPregunta-1
                self.verContenidoPregunta(self.punteroPregunta)
            elif self.contadorPreguntas==0: #ya no sobro ninguna pregunta??..
                self.listWidget_panelPreguntas.setCurrentIndex(4)  # WIDGET VACIO....

            #eliminar el ultimo boton del panel....
            #import ast
            #configuracion=ast.literal_eval(data)#convirtiendo texto a un diccionario
            #with open(nombre) as file:
            #data = file.read()



        '''
        posItemMatar = self.listIdsItemsVivos.index(idItemAMatar)
        resultado = QMessageBox.Yes
        if ordenAutomatica:
            resultado = QMessageBox.question(self, "DelphiPreguntas",
                                             "¿Esta seguro que quieres\n"
                                             f"eliminar el item numero {posItemMatar + 1}?",
                                             QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            layout = self.vbox
            noWidgetBorrar = posItemMatar
            widgetToRemove = layout.itemAt(noWidgetBorrar).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

            self.listaItemsRonianos.pop(posItemMatar)
            self.listIdsItemsVivos.pop(posItemMatar)
            print("Matriz a abortaar", self.matrizEditTextRespuestas.shape)
            self.matrizEditTextRespuestas = np.delete(self.matrizEditTextRespuestas, posItemMatar, 1)
            print("Matriz despues de abortar", self.matrizEditTextRespuestas.shape)
            self.controlABSOLUTO_editTextRespuestas.matrizEditText = self.matrizEditTextRespuestas
            self.punteroNoItems -= 1
        '''




    def getNameDefault(self):
        now = datetime.now()
        # Tiempo apartir del 2020 cuando inicio el juego
        secondYears_50 = 50 * 365 * 24 * 60 * 60
        timeApartir2020 = now.timestamp() - secondYears_50
        redondeo_4 = int(timeApartir2020 * 1000.0)
        return str(redondeo_4)

    def getFecha(self):
        now = datetime.now()
        fecha=now.strftime("%m/%d/%Y,%H:%M:%S")#12/24/2018, 04:59:31
        return fecha


class BotonPregunta(QObject):
    suHoraMorir= pyqtSignal(int)#indicara quien es el objeto que quiere morir...
    clickBotonPregunta=pyqtSignal(int)#indicara el id del boton
    def __init__(self,id,botonPregunta,botonMuerte):
        QObject.__init__(self)
        self.id=id #(numeroPregunta,boton)
        self.botonPregunta=botonPregunta
        self.botonMuerte=botonMuerte
        self.botonPregunta.setText(str(self.id+1))

        self.botonMuerte.clicked.connect(self.mandarSenalMuerto)
        self.botonPregunta.clicked.connect(self.darIdBotonPregunta)


        self.COLOR_NORMAL = "#EAE5E5"
        self.COLOR_SELECCION = "#58C3D0"
        self.BORDER_RADIUS = "7"
        self.botonSeleccionado(False)

    def botonSeleccionado(self,botonPresionado):
        if botonPresionado:
            self.botonPregunta.setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                            f"border-radius:{self.BORDER_RADIUS}px;"
                                                            "border: 0.5px solid #555;")
        else:
            self.botonPregunta.setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                            f"border-radius:{self.BORDER_RADIUS}px;"
                                                            "border: 0.5px solid #555;")

    def mandarSenalMuerto(self):
        self.suHoraMorir.emit(self.id)

    def darIdBotonPregunta(self):
        self.clickBotonPregunta.emit(self.id)







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    #FORMA DE TENER ACCESO AL STORAGE...
    #direccionJson = RecursosMenuDelphiApp.DIRE_JSON
    #nombreStorage = 'delphiadata.appspot.com'
    #storage_client = storage.Client.from_service_account_json(direccionJson)
    #bucket = storage_client.get_bucket(nombreStorage)

    application = CreadorPreguntas(nombreCreador="Roni",
                                   nombreCuestionario="Roni")
    application.show()
    app.exec()
    #sys.exit(app.exec())

'''
    
    #https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE


        self.btn_aplicarTam.clicked.connect(self.changedSize)

        self.vSlider_image.sliderMoved.connect(self.changedSizeImage)
        self.btn_mas.clicked.connect(self.crearOtraPregunta)

    def crearOtraPregunta(self):
        self.ventanaMenuPregunta=menuTipoPreguntas()
        self.ventanaMenuPregunta.usuarioEscogioPregunta.connect(self.escogioPregunta)
        self.ventanaMenuPregunta.show()





    def changedSizeImage(self,valor):
        self.txtEdit_preg.setMaximumSize(100,valor*3)
        self.txtEdit_preg.setMinimumSize(100,valor*3)

    def changedSize(self):





'''