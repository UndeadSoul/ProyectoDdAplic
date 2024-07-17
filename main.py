#imports
from os import system
from functions.connectMySql import *
from functions.vendedor import *
from functions.jefedeventas import *


#create db
db=Database()
#main menu
while True:
    system("cls")
    user=input("Ingrese Usuario: ")
    password=input("ingrese Contraseña: ")
    typeOfUser=credentials(user,password,db)
    system("cls")
    match typeOfUser.lower():
        case "vendedor":
            input(f"Bienvenido Vendedor {user} \
                  \npresione Enter para ingresar al menu")
            sellerMenu(user,db)
        case "jefedeventas":
            input(f"Bienvenido Jefe de ventas {user} \
                  \npresione Enter para ingresar al menu...")
            salesManagerMenu(user,db)
        case _:
            system("cls")
            input("Las credenciales entregadas no coinciden con ninguna en nuestra base de datos.\
                  \nPresione Enter para intentar nuevamente")
    #this should be the main menu where the program starts and goes to the specific menus
