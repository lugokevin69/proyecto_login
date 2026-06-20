import mysql.connector  #Importamos el conector de mysql para poder conectar a la base de datos.

def conectar():  #Esta funcion conecta con la base de datos.
    return mysql.connector.connect(
        host="Localhost",    #Si no funciona "Localhost" pruebar con "127.0.0.1"
        port=3305,
        user="root",
        password="contra2005", 
        database="instituto",
        use_pure=True      #Utiliza la implementacion pura en python y no deja que se cierre al guardar.
    )