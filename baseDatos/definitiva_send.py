import sqlite3

"""
miCursor.execute('''
        CREATE TABLE PREGUNTAS(
        ID_PREGUNTA INTEGER,
        MUTACION INTEGER,
        PREG_TEXT VARCHAR(50),
        PREG_IMAG VARCHAR(50),
        RESPA_TEXT VARCHAR(50),
        RESPA_IMAG VARCHAR(50),
        RESPB_TEXT VARCHAR(50),
        RESPB_IMAG VARCHAR(50),
        RESPC_TEXT VARCHAR(50),
        RESPC_IMAG VARCHAR(50),
        RESPD_TEXT VARCHAR(50),
        RESPD_IMAG VARCHAR(50) )
       '''
)
"""

miConexion=sqlite3.connect("Multiples")
miCursor=miConexion.cursor()

productos=[
    (10, 2, "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola"),
    (10, 2, "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola"),
    (10, 2, "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola"),
    (10, 2, "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola"),
    (10, 2, "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola")
]

#como podemos ver en la seccion de clave, pusimos un NULL ya que de esa
#manera le indicamos a python que no ponemos dato ahi,porque es el que
#el generara como ID
#Dentro de la funcion va la instruccion SQLITE
miCursor.executemany("INSERT INTO PREGUNTAS VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",productos)

#Confirmamos los cambios...
miConexion.commit()
miConexion.close()

#¿QUE PASO SI INGRESO UN DATO CON UNA CLAVE QUE YA EXISTE?
#Marcara error porque esa clave ya existe..
