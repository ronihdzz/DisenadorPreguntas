import ast
import pyrebase
import zipfile
'''
from PyQt5 import QtWidgets
import sys
from os import getcwd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QFileDialog, QLineEdit
from PyQt5.QtCore import Qt


ext = imagen.split(".")
self.storage.child("images/"+self.usuario+'.'+ext[1]).put(imagen)
self.db.child("INTEGRANTES").child(self.usuario).update({'Imagen':self.usuario+'.'+ext[1]})
self.storage.child("images/"+self.usuario+'.'+ext[1]).download(filename=self.usuario+'.'+ext[1],path=getcwd())



with open(nombre) as file:
    data = file.read()

configuracion=ast.literal_eval(data)#convirtiendo texto a un diccionario
pyBase = pyrebase.initialize_app(configuracion)
auth= pyBase.auth()
storage= pyBase.storage()
db =pyBase.database()

storage.child("Roni.db").put("Roni.db")
#self.storage.child("images/"+self.usuario+'.'+ext[1]).put(imagen)
#ast.literal_eval(respuesta)#convirtiendo texto a un diccionario
'''
nombre="../../../../RECURSOS/Datos_BaseDatos_Delphi.txt"
with open(nombre) as file:
    data = file.read()

configuracion=ast.literal_eval(data)#convirtiendo texto a un diccionario
pyBase = pyrebase.initialize_app(configuracion)
auth= pyBase.auth()
storage= pyBase.storage()
db =pyBase.database()

#ver la lista de contenidos del storage...

#files = storage.child("images").list_files()
#for file in files:
#    print(file)


#storage.delete("Roni.db")



#storage.child("Ronaldo.zip").put("Ronaldo.zip")
#self.storage.child("images/"+self.usuario+'.'+ext[1]).put(imagen)

#ast.literal_eval(respuesta)#convirtiendo texto a un diccionario


















'''

# import required modules

import os
import zipfile


# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths


# Declare the main function
def main():
    # Assign the name of the directory to zip
    dir_name = "Roni"

    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(dir_name)

    # printing the list of all files to be zipped
    print('The following list of files will be zipped:')
    for fileName in filePaths:
        print(fileName)

    # writing files to a zipfile
    zip_file = zipfile.ZipFile(dir_name + '.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            zip_file.write(file)

    print(dir_name + '.zip file is created successfully!')

#https://linuxhint.com/python_zip_file_directory/
# Call the main function
if __name__ == "__main__":
    main()
    
#Decomprimir...
# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "Ronaldo.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')

https://www.geeksforgeeks.org/working-zip-files-python/




'''


