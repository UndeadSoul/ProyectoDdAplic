#imports
from os import system
from functions.connectMySql import *
from functions.vendedor import *
from functions.jefedeventas import *
from pwinput import pwinput

#create db
db=Database()
#main menu
while True:
    system("cls")
    #para ingresar por defecto al jefedeventas user=adminjdv password=contramysql
    #para ingresar por defecto al vendedor user=admin password=contramysql
    user=input("Ingrese Usuario: ")
    password=pwinput("ingrese Contraseña: ")
    typeOfUser=credentials(user,password,db)
    system("cls")
    match typeOfUser.lower():
        case "vendedor":
            if estadocheck(db).lower()=="abierto":
                input(f"Bienvenido Vendedor {user} \
                    \nPresione Enter para ingresar al menu... ")
                sellerMenu(user,db)
            else:
                print("El estado del Bazar se encuentra actualmente cerrado, contactese con su jefe de ventas. ")
                input("Presione Enter para volver al inicio... ")
        case "jefedeventas":
            input(f"Bienvenido Jefe de ventas {user} \
                  \nPresione Enter para ingresar al menu... ")
            salesManagerMenu(user,db)
        case _:
            system("cls")
            input("Las credenciales entregadas no coinciden con ninguna en nuestra base de datos.\
                  \nPresione Enter para intentar nuevamente")
