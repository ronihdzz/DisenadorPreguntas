import os
import ast
###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios


class CuestionariosDelphi:
    def __init__(self):
        pass



#Returna una lista de diccionarios con los datos de cada cuestionario, pero
#cabe mencionar que la lista esta ordenada del mas reciente al mas antiguo
    @staticmethod
    def getNombresCuestionarios(descargados=False,mios=False,oficiales=False,compartidos=False):

        #solo funcionara si solo uno de los tres es true...
        if descargados+mios+oficiales+compartidos==1:
            if descargados:
                direc=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS
            elif mios:
                direc=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION
            elif oficiales:
                direc=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES
            elif compartidos:
                direc=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS

            #obteniendo nombres de carpetas y archivos en esa ruta...
            a = os.listdir(direc)
            dictDataCuestionarios = {}# DATA_TIME,'PREGUNTAS':
            valoresOrden=[] #almacenara los  valores de orden...
            for x in a:
                nombre = direc + x
                if os.path.isdir(nombre):#solo almacenando carpeta
                    nameFileDatos=nombre+"/"+x+".txt"
                    with open(nameFileDatos,'r') as file:
                        data = file.read()
                    dictData=ast.literal_eval(data)
                    dictData["NOMBRE"]=x

                    dictDataCuestionarios[int(dictData["ORDEN"])]=dictData

            tuplaDataOrdenada=sorted(dictDataCuestionarios.items(),reverse=True)

            tuplaDataOrdenada=[a[1] for a in tuplaDataOrdenada]

            return tuplaDataOrdenada