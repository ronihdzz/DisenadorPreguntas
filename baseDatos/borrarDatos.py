import sqlite3


#Abriendo o crenado conexion
miConexion=sqlite3.connect("Jorge")

#Puntero de la base...
miCursor=miConexion.cursor()
#SELECT * ==>NOS DEVUELVE TODOS LOS PRODUCTOS...
sql = 'DELETE FROM PRODUCTOS LIMIT 5,1;'
#sql="select * from tablename order by id limit 1;"
#sql="DELETE FROM PRODUCTOS OFFSET=3"
miCursor.execute(sql)
#Confirmamos los cambios...
miConexion.commit()

miConexion.close()