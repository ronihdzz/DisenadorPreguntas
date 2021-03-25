import os

class RecursosCreadorCuestionarios():

    direc_carpetaRecuersos="../../../RECURSOS/"
    direc_carpeta=direc_carpetaRecuersos+"IMAG_CREADOR_PREGUNTAS/"
    DIRE_JSON=direc_carpetaRecuersos+"firebase-sdk.json"


    # Apartir de la carpeta de recursos corrabolaremos que tengamos los siguientes datos
    direcCuestionarios = direc_carpetaRecuersos + "DATOS_DE/" + "ANONIMO" + "/" + "CUESTIONARIOS/"
    # crea estos directorios, en caso dE ya existir no hacer nada...
    os.makedirs(direcCuestionarios + "COMPARTIDOS", exist_ok=True)
    # crea estos directorios, en caso dE ya existir no hacer nada...
    os.makedirs(direcCuestionarios + "DESCARGADOS", exist_ok=True)
    # crea estos directorios, en caso dE ya existir no hacer nada...
    os.makedirs(direcCuestionarios + "EDITADOS", exist_ok=True)

# N O M B R E S :
    NOMBRE_STORAGE = "delphiadata.appspot.com"
    DIREC_CUESTIONARIOS_STORAGE = "CUESTIONARIOS/"
    DIREC_DELPHITEST_STORAGE="TEST_DELPHIA/"
    ID_CARPETA_IMAGENES="IMAG_"
    TERMINACION_CUESTIONARIOS="_delron"


# O T R A S    C A R P E T A S :

    # C U E S T I O N A R I O S   O F I C I A L E S :
    DIREC_CUESTIONARIOS_DELPHI_OFICIALES = direc_carpetaRecuersos + "DELPHI_TEST/"

    # C U E S T I O N A R I O S :

    DIREC_CUESTIONARIOS_EDICION= direcCuestionarios+"EDITADOS/"
    DIREC_CUESTIONARIOS_DESCARGADOS=direcCuestionarios+"DESCARGADOS/"
    DIREC_CUESTIONARIOS_COMPARTIDOS=direcCuestionarios+"COMPARTIDOS/"


    FILE_DATOS_BASEDATOS_DELPHI=direc_carpetaRecuersos+"Datos_BaseDatos_Delphi.txt"


#C A R P E T A     D E    I M A G E N E S  :
    ICONO_INCLUIR_IMAGENES_0 = direc_carpeta + "icon_preg0.png"
    ICONO_INCLUIR_IMAGENES_50 = direc_carpeta + "icon_preg50.png"
    ICONO_INCLUIR_IMAGENES_75 = direc_carpeta + "icon_preg75.png"
    ICONO_INCLUIR_IMAGENES_100 = direc_carpeta + "icon_preg100.png"

    ICONO_PREG_AND = direc_carpeta + "icon_and.png"
    ICONO_PREG_OR = direc_carpeta + "icon_or.png"

    ICONO_POS_LEFT = direc_carpeta + "alinear_izquierda.png"
    ICONO_POS_CENTER = direc_carpeta + "alinear_centrar.png"
    ICONO_POS_RIGTH = direc_carpeta + "alinear_derecho.png"

    ICONO_TACHE = direc_carpeta + "icon_tache.png"
    ICONO_TACHE_2 = direc_carpeta + "icon_tache2.png"

    ICONO_RESP_STRING=direc_carpeta+"icon_respPalabra.png"
    ICONO_RESP_NUMBER=direc_carpeta+"icon_respNumber.png"

    ICONO_IMAGEN_DEFAULT=direc_carpeta+"icon_escogerImagen.png"

    ICON_IMAGEN_PREG_BINARIA=direc_carpeta+"icon_pregTrueFalse.png"
    ICON_IMAGEN_PREG_MULTIPLE = direc_carpeta+"icon_pregMultiple.png"
    ICON_IMAGEN_PREG_CHECKBOX = direc_carpeta+"icon_pregItems.png"
    ICON_IMAGEN_PREG_ABIERTA = direc_carpeta+"icon_pregAbierta.png"

    ICON_RESPONDI_YO=direc_carpeta+"icon_yoDije.png"
    ICON_RESPONDIO_EL=direc_carpeta+"icon_yoNoDije.png"

    ICON_CUESTIONARIOS_DESCARGADOS=direc_carpeta+"cuestionariosDescargados"
    ICON_CUESTIONARIOS_PROCESO=direc_carpeta+"cuestionariosProceso"

    ICON_RESPONDIO_BIEN=direc_carpeta+"icon_respBuena.png"
    ICON_RESPONDIO_MAL=direc_carpeta+"icon_respMala.png"


    def __init__(self):
        pass


    @staticmethod
    def cambiarDireccion(newDirecRecursos="",user=""):
        #RecursosCreadorCuestionarios.direc_carpetaRecuersos = "../../../RECURSOS/"


        #Apartir de la carpeta de recursos corrabolaremos que tengamos los siguientes datos
        direcCuestionarios=newDirecRecursos+"DATOS_DE/"+user+"/"+"CUESTIONARIOS/"
        # crea estos directorios, en caso dE ya existir no hacer nada...
        os.makedirs(direcCuestionarios+"COMPARTIDOS", exist_ok=True)
        # crea estos directorios, en caso dE ya existir no hacer nada...
        os.makedirs(direcCuestionarios+"DESCARGADOS", exist_ok=True)
        # crea estos directorios, en caso dE ya existir no hacer nada...
        os.makedirs(direcCuestionarios+"EDITADOS", exist_ok=True)


        direc_carpetaRecuersos=newDirecRecursos
        direc_carpeta=direc_carpetaRecuersos + "IMAG_CREADOR_PREGUNTAS/"


        RecursosCreadorCuestionarios.direc_carpetaRecuersos = newDirecRecursos
        RecursosCreadorCuestionarios.direc_carpeta = direc_carpetaRecuersos + "IMAG_CREADOR_PREGUNTAS/"
        RecursosCreadorCuestionarios.DIRE_JSON = direc_carpetaRecuersos + "firebase-sdk.json"


        # N O M B R E S :
        RecursosCreadorCuestionarios.NOMBRE_STORAGE = "delphiadata.appspot.com"
        RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_STORAGE = "CUESTIONARIOS/"
        RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES = "IMAG_"
        RecursosCreadorCuestionarios.TERMINACION_CUESTIONARIOS = "_delron"


        # O T R A S    C A R P E T A S :

        # C U E S T I O N A R I O S   O F I C I A L E S :
        RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES = direc_carpetaRecuersos + "DELPHI_TEST/"


        # C A R P E T A S   D E   C U E S T I O N A R I O S :

        RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION = direcCuestionarios + "EDITADOS/"
        RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS = direcCuestionarios + "DESCARGADOS/"
        RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS = direcCuestionarios + "COMPARTIDOS/"


        RecursosCreadorCuestionarios.FILE_DATOS_BASEDATOS_DELPHI = direc_carpetaRecuersos + "Datos_BaseDatos_Delphi.txt"

        # C A R P E T A     D E    I M A G E N E S  :
        RecursosCreadorCuestionarios.ICONO_INCLUIR_IMAGENES_0 = direc_carpeta + "icon_preg0.png"
        RecursosCreadorCuestionarios.ICONO_INCLUIR_IMAGENES_50 = direc_carpeta + "icon_preg50.png"
        RecursosCreadorCuestionarios.ICONO_INCLUIR_IMAGENES_75 = direc_carpeta + "icon_preg75.png"
        RecursosCreadorCuestionarios.ICONO_INCLUIR_IMAGENES_100 = direc_carpeta + "icon_preg100.png"

        RecursosCreadorCuestionarios.ICONO_PREG_AND = direc_carpeta + "icon_and.png"
        RecursosCreadorCuestionarios.ICONO_PREG_OR = direc_carpeta + "icon_or.png"

        RecursosCreadorCuestionarios.ICONO_POS_LEFT = direc_carpeta + "alinear_izquierda.png"
        RecursosCreadorCuestionarios.ICONO_POS_CENTER = direc_carpeta + "alinear_centrar.png"
        RecursosCreadorCuestionarios.ICONO_POS_RIGTH = direc_carpeta + "alinear_derecho.png"

        RecursosCreadorCuestionarios.ICONO_TACHE = direc_carpeta + "icon_tache.png"
        RecursosCreadorCuestionarios.ICONO_TACHE_2 = direc_carpeta + "icon_tache2.png"

        RecursosCreadorCuestionarios.ICONO_RESP_STRING = direc_carpeta + "icon_respPalabra.png"
        RecursosCreadorCuestionarios.ICONO_RESP_NUMBER = direc_carpeta + "icon_respNumber.png"

        RecursosCreadorCuestionarios.ICONO_IMAGEN_DEFAULT = direc_carpeta + "icon_escogerImagen.png"

        RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_BINARIA = direc_carpeta + "icon_pregTrueFalse.png"
        RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_MULTIPLE = direc_carpeta + "icon_pregMultiple.png"
        RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_CHECKBOX = direc_carpeta + "icon_pregItems.png"
        RecursosCreadorCuestionarios.ICON_IMAGEN_PREG_ABIERTA = direc_carpeta + "icon_pregAbierta.png"

        RecursosCreadorCuestionarios.ICON_RESPONDI_YO = direc_carpeta + "icon_yoDije.png"
        RecursosCreadorCuestionarios.ICON_RESPONDIO_EL = direc_carpeta + "icon_yoNoDije.png"

        RecursosCreadorCuestionarios.ICON_CUESTIONARIOS_DESCARGADOS = direc_carpeta + "cuestionariosDescargados"
        RecursosCreadorCuestionarios.ICON_CUESTIONARIOS_PROCESO = direc_carpeta + "cuestionariosProceso"

        RecursosCreadorCuestionarios.ICON_RESPONDIO_BIEN = direc_carpeta + "icon_respBuena.png"
        RecursosCreadorCuestionarios.ICON_RESPONDIO_MAL = direc_carpeta + "icon_respMala.png"