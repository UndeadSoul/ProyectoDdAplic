import mysql.connector
from functions.connectMySql import Database
from functions.setupfunc import *

db=""
nombredb="nona"
#verificar si existe database
if(dbDoesntExist(nombredb)):
    #hacer el setup de la base de datos
    createDb(nombredb)
    #obtener la direccion de la base de datos
    db=Database()
    #ingresar los script de las tablas
    createTables(db)
    db.cerrarBD()
    db=Database()
    defaultValues(db)
    db.cerrarBD()
    print("Setup de base de datos completado")
    input("Presione enter para terminar... ")
else:
    print("La base de datos ya se encuentra creada")
    input("Presione enter para continuar... ")


