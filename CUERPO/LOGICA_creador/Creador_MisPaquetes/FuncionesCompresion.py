from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
import shutil
import os
import zipfile

# importing required modules
from zipfile import ZipFile
import os

# importing required modules
from zipfile import ZipFile



def descomprimirZip(file_name):
    # specifying the zip file name
    file_name+=".zip"
    # opening the zip file in READ mode
    with ZipFile(file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')

# Declare la función para devolver todas las rutas de archivo del directorio en particular
def retrieve_file_paths(dirName):
    # variable de rutas de archivo de configuración
    filePaths = []

    # Leer todos los directorios, subdirectorios y listas de archivos
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Cree la ruta de archivo completa utilizando el módulo os.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # devuelve todos los caminos
    print(filePaths)
    return filePaths


# Declare the main function
def comprimirCarpeta(dir_name):
    # Llame a la función para recuperar todos los archivos y carpetas del directorio asignado
    filePaths = retrieve_file_paths(dir_name)

    # imprimir la lista de todos los archivos a comprimir
    print('Se comprimirá la siguiente lista de archivos:')
    for fileName in filePaths:
        print(fileName)

    # escribir archivos en un archivo zip
    zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
    with zip_file:
        # escribiendo cada archivo uno por uno
        for file in filePaths:
            zip_file.write(file)
    print(dir_name + '¡El archivo .zip se creó correctamente!')





