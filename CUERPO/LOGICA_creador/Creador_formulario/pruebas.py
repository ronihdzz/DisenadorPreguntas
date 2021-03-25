from CUERPO.LOGICA_creador.Creador_formulario.DataBase_formulario import DataBase_formulario

roni=DataBase_formulario("DATA")

#Creando la base de datos
roni.crearBaseDatos()
#roni.addUsuario("Julian",21,"1928374655","fenfelipe")
#print(roni.getAll_datos(EDAD=True,CLAVE=True,AMIGO=True))
roni.actualizarDatos(DE="Roni",AMIGO="PENESgrandes")
#print(roni.getAll_datos(AMIGO=True))

#roni.addUsuario( ("CULO",19,"123","felipe") )

#a=roni.getAll_datos()
#roni.eliminarUsuario(nombreUsuario="pENEvenoso")


#x=roni.getDatosUsuario(nombreUsuario="Pedro")
#print(x)

#roni.actualizarDatosDe(new_nombre_usuario="Jaime",nombre_usuario="PedroYRoni",new_edad=300,new_clave="MEME")
#roni.actualizarDatosDe(nombre="Pedro",edad=100)