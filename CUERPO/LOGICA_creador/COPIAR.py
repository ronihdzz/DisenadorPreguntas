import shutil, os

ruta = os.getcwd() + os.sep
origen =  'Creador_Ejecutador/'
destino = 'RONI/'


if os.path.exists(origen):
        listaArchivos=os.listdir(origen)
        for x in listaArchivos:
                print(x)
                if '.' in x: #los nombres de las imagenes tienen puntos...
                        archivoCopeara=origen+x
                        lugarDondeGuardara=destino+x
                        shutil.copy(archivoCopeara,lugarDondeGuardara)



#https://unipython.com/operaciones-con-archivos-y-carpetas-en-python/

#https://micro.recursospython.com/recursos/como-eliminar-un-archivo-o-carpeta.html

