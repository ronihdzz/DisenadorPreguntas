import sqlite3



miConexion=sqlite3.connect("Jorge")
miCursor=miConexion.cursor()

"""
    #CUANDO QUEREMOS QUE LAS CLAVES SEA AUTOMATICAS
    #POR CONVENCION SE LES SUELE ASIGNAR EL NOMBRE DE ID..
    #PRIMARY KEY==>ATRIBUTO QUE SERA LA LLAVE
    #AUTOINCREMENT ==>Los id se iran enumerando
    miCursor.execute('''
        CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    '''
    )
"""


#ya no necesitamos la seccion de CLAVE, por eso
#cada tupla solo tiene un elemento...
productos=[
    ("Roni",20,"Apasionado"),
    ("Fransico",22,"Emprendedor"),
    ("Julian",23,"Curioso")
]

#como podemos ver en la seccion de clave, pusimos un NULL ya que de esa
#manera le indicamos a python que no ponemos dato ahi,porque es el que
#el generara como ID
#Dentro de la funcion va la instruccion SQLITE
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

#Confirmamos los cambios...
miConexion.commit()
miConexion.close()

#¿QUE PASO SI INGRESO UN DATO CON UNA CLAVE QUE YA EXISTE?
#Marcara error porque esa clave ya existe..
